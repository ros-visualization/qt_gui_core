# Copyright 2026 jcfurey
# SPDX-License-Identifier: BSD-3-Clause

from functools import partial
from types import SimpleNamespace

import pytest
from python_qt_binding.QtCore import QCoreApplication, QSettings

from qt_gui.plugin_handler_direct import PluginHandlerDirect
from qt_gui.plugin_instance_id import PluginInstanceId
from qt_gui.plugin_manager import PluginManager
from qt_gui.settings import Settings
from qt_gui.settings_proxy import SettingsProxy


class RecordingPlugin:
    """Record lifecycle calls without creating widgets."""

    def __init__(self, name, events):
        self.name = name
        self.events = events

    def save_settings(self, plugin_settings, instance_settings):
        """Record that settings were saved."""
        self.events.append(('save', self.name))

    def shutdown_plugin(self):
        """Record that shutdown completed."""
        self.events.append(('shutdown', self.name))


class RecordingProvider:
    """Track the plugin instances still held when the provider shuts down."""

    def __init__(self, events):
        self.events = events
        self.instances = {}

    def unload(self, plugin):
        """Release an instance using the normal direct-handler unload path."""
        self.instances.pop(plugin.name)
        self.events.append(('unload', plugin.name))

    def shutdown(self):
        """Record remaining instances before the provider is destroyed."""
        self.events.append(('providers', tuple(self.instances)))


class DeferredHandler(PluginHandlerDirect):
    """Delay selected lifecycle completions while retaining real handler callbacks."""

    def __init__(self, *args, deferred):
        super().__init__(*args)
        self.deferred = deferred
        self.pending = {}

    def _complete_or_defer(self, stage, call):
        if stage in self.deferred:
            self.pending[stage] = call
        else:
            call()

    def _save_settings(self, plugin_settings, instance_settings):
        self._complete_or_defer('save', partial(
            super()._save_settings, plugin_settings, instance_settings))

    def _shutdown_plugin(self):
        self._complete_or_defer('shutdown', super()._shutdown_plugin)

    def _unload(self):
        self._complete_or_defer('unload', super()._unload)

    def complete(self, stage):
        """Finish one pending call through the production handler."""
        self.pending.pop(stage)()


@pytest.fixture(scope='session', autouse=True)
def application():
    """Keep the Qt application alive for all QObject instances."""
    return QCoreApplication.instance() or QCoreApplication([])


@pytest.fixture
def make_manager(tmp_path):
    """Build a manager with already-loaded direct or deferred plugin handlers."""
    def make(deferred_stages):
        events = []
        provider = RecordingProvider(events)
        context = SimpleNamespace(
            options=SimpleNamespace(
                multi_process=False, embed_plugin=False,
                lock_perspective=False, standalone_plugin=None),
            provide_app_dbus_interfaces=False)
        qsettings = QSettings(str(tmp_path / 'settings.ini'), QSettings.Format.IniFormat)
        manager = PluginManager(provider, qsettings, context)
        settings = Settings(SettingsProxy(qsettings), '')
        manager.close_application_signal.connect(
            lambda: events.append(('closed', tuple(manager._running_plugins))))
        handlers = []
        for serial, stages in enumerate(deferred_stages, start=1):
            instance_id = PluginInstanceId('TestPlugin', serial)
            name = str(instance_id)
            args = (manager, None, instance_id, context, None, [])
            handler = DeferredHandler(*args, deferred=stages) if stages else \
                PluginHandlerDirect(*args)
            plugin = RecordingPlugin(name, events)
            handler._plugin = plugin
            handler._plugin_provider = provider
            provider.instances[name] = plugin
            manager._running_plugins[name] = {'instance_id': instance_id, 'handler': handler}
            handler.close_signal.connect(manager.unload_plugin)
            handlers.append(handler)
        return SimpleNamespace(
            manager=manager, provider=provider, settings=settings,
            handlers=handlers, events=events,
            close=lambda: manager.close_application(settings, settings))
    return make


def assert_closed(state):
    """Require all instances to be released before providers and the application close."""
    assert state.events[-2:] == [('providers', ()), ('closed', ())]
    assert [event for event in state.events if event[0] == 'providers'] == [('providers', ())]
    assert [event for event in state.events if event[0] == 'closed'] == [('closed', ())]
    assert not state.provider.instances
    assert not state.manager._running_plugins
    assert all(handler._plugin is None for handler in state.handlers)
    assert state.manager._number_of_ongoing_calls is None


@pytest.mark.parametrize('count', [0, 1, 3])
def test_close_synchronous_plugins(make_manager, count):
    """Close empty, single-plugin and multi-plugin applications synchronously."""
    state = make_manager([set() for _ in range(count)])
    state.close()
    names = [str(handler.instance_id()) for handler in state.handlers]
    assert state.events == [
        (stage, name) for stage in ('save', 'shutdown', 'unload') for name in names
    ] + [('providers', ()), ('closed', ())]
    assert_closed(state)


@pytest.mark.parametrize('stage', ['save', 'shutdown'])
def test_wait_for_all_callbacks(make_manager, stage):
    """Wait for every save or shutdown callback before starting the next phase."""
    state = make_manager([{stage}, {stage}])
    state.close()
    phases_before = [] if stage == 'save' else ['save', 'save']
    assert [event[0] for event in state.events] == phases_before
    state.handlers[1].complete(stage)
    assert [event[0] for event in state.events] == phases_before + [stage]
    assert len(state.manager._running_plugins) == 2
    state.handlers[0].complete(stage)
    assert_closed(state)
    phases = [event[0] for event in state.events]
    assert phases == ['save'] * 2 + ['shutdown'] * 2 + ['unload'] * 2 + [
        'providers', 'closed']


def test_wait_for_unload_callbacks(make_manager):
    """Remove each plugin on unload completion and close only after the last one."""
    state = make_manager([{'unload'}, {'unload'}])
    state.close()
    assert [event[0] for event in state.events] == ['save'] * 2 + ['shutdown'] * 2
    state.handlers[1].complete('unload')
    remaining = str(state.handlers[0].instance_id())
    assert list(state.manager._running_plugins) == [remaining]
    assert list(state.provider.instances) == [remaining]
    assert state.events[-1] == ('unload', str(state.handlers[1].instance_id()))
    state.handlers[0].complete('unload')
    assert_closed(state)


def test_mixed_synchronous_and_deferred_plugins(make_manager):
    """Handle synchronous dictionary changes around a plugin with delayed callbacks."""
    state = make_manager([set(), {'save', 'shutdown', 'unload'}, set()])
    delayed = state.handlers[1]
    state.close()
    assert [event[0] for event in state.events] == ['save', 'save']
    delayed.complete('save')
    assert [event[0] for event in state.events] == ['save'] * 3 + ['shutdown'] * 2
    delayed.complete('shutdown')
    assert [event[0] for event in state.events] == ['save'] * 3 + ['shutdown'] * 3 + [
        'unload', 'unload']
    assert list(state.manager._running_plugins) == [str(delayed.instance_id())]
    delayed.complete('unload')
    assert_closed(state)
