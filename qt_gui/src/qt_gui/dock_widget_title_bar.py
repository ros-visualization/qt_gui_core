# Copyright (c) 2011, Dirk Thomas, Dorian Scholz, TU Darmstadt
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of the TU Darmstadt nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os

from python_qt_binding import loadUi
from python_qt_binding.QtCore import QEvent, QObject, Qt, qWarning
from python_qt_binding.QtGui import QDockWidget, QIcon, QWidget


class DockWidgetTitleBar(QWidget):

    """Title bar for dock widgets providing custom actions."""

    def __init__(self, dock_widget, qtgui_path):
        super(DockWidgetTitleBar, self).__init__(dock_widget)
        self._dock_widget = dock_widget

        ui_file = os.path.join(qtgui_path, 'resource', 'dock_widget_title_bar.ui')
        loadUi(ui_file, self)
        self._extra_buttons = {
            'configuration': self.configuration_button,
            'reload': self.reload_button,
            'help': self.help_button,
            'close': self.close_button,
        }

        icon = QIcon.fromTheme('emblem-system')
        if not icon.isNull():
            self.configuration_button.setIcon(icon)
            self.configuration_button.setText("")
        icon = QIcon.fromTheme('view-refresh')
        if not icon.isNull():
            self.reload_button.setIcon(icon)
            self.reload_button.setText("")
        icon = QIcon.fromTheme('help-browser')
        if not icon.isNull():
            self.help_button.setIcon(icon)
            self.help_button.setText("")

        icon = QIcon.fromTheme('window-close')
        if not icon.isNull():
            self.close_button.setIcon(icon)
            self.close_button.setText("")
        self.close_button.clicked.connect(self._close_clicked)

        self.float_button.clicked.connect(self._toggle_floating)
        self.dockable_button.clicked[bool].connect(self._toggle_dockable)
        self.minimize_button.clicked.connect(self._minimize_dock_widget)

        self._dock_widget.featuresChanged.connect(self._features_changed)
        self._features_changed()

        self._update_icon()
        self._update_title()

        self._close_callbacks = []
        self._event_callbacks = {
            QEvent.WindowIconChange: self._update_icon,
            QEvent.WindowTitleChange: self._update_title,
        }
        self._dock_widget.installEventFilter(self)

    def __del__(self):
        self._dock_widget.removeEventFilter(self)

    def connect_button(self, button_id, callback):
        button = self._extra_buttons.get(button_id, None)
        if button is None:
            qWarning('DockWidgetTitleBar.connect_button(): unknown button_id: %s' % button_id)
            return
        button.clicked.connect(callback)

    def connect_close_button(self, callback):
        self._close_callbacks.append(callback)

    def _close_clicked(self):
        for callback in self._close_callbacks:
            callback(self.parent())

    def show_button(self, button_id, visibility=True):
        button = self._extra_buttons.get(button_id, None)
        if button is None:
            qWarning('DockWidgetTitleBar.show_button(): unknown button_id: %s' % button_id)
            return
        button.setVisible(visibility)

    def hide_button(self, button_id):
        self.show_button(button_id, False)

    def eventFilter(self, obj, event):
        if event.type() in self._event_callbacks:
            ret_val = self._event_callbacks[event.type()](obj, event)
            if ret_val is not None:
                return ret_val
        return QObject.eventFilter(self, obj, event)

    def _update_icon(self, *args):
        pixmap = None
        if self.parentWidget().windowIcon():
            pixmap = self.parentWidget().windowIcon().pixmap(self.close_button.iconSize())
        self.icon_label.setPixmap(pixmap)

    def _update_title(self, *args):
        self.title_label.setText(self.parentWidget().windowTitle())

    def _toggle_dockable(self, enabled):
        dock_widget = self.parentWidget()
        if enabled:
            dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)
        else:
            dock_widget.setAllowedAreas(Qt.NoDockWidgetArea)

    def _toggle_floating(self):
        dock_widget = self.parentWidget()
        dock_widget.setFloating(not dock_widget.isFloating())

    def _minimize_dock_widget(self):
        dock_widget = self.parentWidget()
        dock_widget.hide()

    def _features_changed(self, features=None):
        if features is None:
            features = self.parentWidget().features()

        closable = bool(features & QDockWidget.DockWidgetClosable)
        self.close_button.setVisible(closable)
        self.reload_button.setVisible(closable)

        movable = bool(features & QDockWidget.DockWidgetMovable)
        self.dockable_button.setChecked(movable)
        self._toggle_dockable(self.dockable_button.isChecked())
        self.dockable_button.setVisible(movable)
        self.float_button.setVisible(movable)
        self.minimize_button.setVisible(movable)

    def save_settings(self, settings):
        # skip saving dockable flag when layout is frozen
        movable = bool(self.parentWidget().features() & QDockWidget.DockWidgetMovable)
        if movable:
            settings.set_value('dockable', self.dockable_button.isChecked())

    def restore_settings(self, settings):
        dockable = settings.value('dockable', True) in [True, 'true']
        # only allow dockable when layout is not frozen
        movable = bool(self.parentWidget().features() & QDockWidget.DockWidgetMovable)
        self.dockable_button.setChecked(dockable and movable)
        self._toggle_dockable(self.dockable_button.isChecked())


if __name__ == '__main__':
    import sys
    from python_qt_binding.QtGui import QApplication
    from .dockable_main_window import DockableMainWindow

    app = QApplication(sys.argv)

    win = DockableMainWindow()

    dock1 = QDockWidget('dockwidget1', win)
    win.addDockWidget(Qt.LeftDockWidgetArea, dock1)
    title_bar = DockWidgetTitleBar(dock1)
    dock1.setTitleBarWidget(title_bar)

    dock2 = QDockWidget('dockwidget2')
    win.addDockWidget(Qt.RightDockWidgetArea, dock2)
    title_bar = DockWidgetTitleBar(dock2)
    dock2.setTitleBarWidget(title_bar)

    win.resize(640, 480)
    win.show()

    app.exec_()
