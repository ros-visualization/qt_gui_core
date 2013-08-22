^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package qt_gui
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.2.17 (2013-08-21)
-------------------
* add PluginLoadError for know errors to avoid printing stacktraces (`ros-visualization/rqt#85 <https://github.com/ros-visualization/rqt/issues/85>`_)
* inherit icons from plugin menu for dock widgets
* fix several OS X related rendering issues, mostly icons and bring the window to front on startup (`ros-visualization/rqt#83 <https://github.com/ros-visualization/rqt/issues/83>`_)
* fix about dialog to not show application icon

0.2.16 (2013-06-06)
-------------------
* make plugin resources relative to plugin.xml (instead of package.xml) (`#16 <https://github.com/ros-visualization/qt_gui_core/issues/16>`_)
* add feature to minimize dock widgets (`#13 <https://github.com/ros-visualization/qt_gui_core/issues/13>`_)
* add feature that each each dock widget can show its own window icon (`#19 <https://github.com/ros-visualization/qt_gui_core/issues/19>`_)
* add option '--perspective-file' to load exported perspective from a file via cli (`#18 <https://github.com/ros-visualization/qt_gui_core/issues/18>`_)
* add option '-f' to freeze layout of dock widgets (`#21 <https://github.com/ros-visualization/qt_gui_core/issues/21>`_)
* restrict reparenting to specific main windows, prevent reparenting into arbitrary main windows (`#14 <https://github.com/ros-visualization/qt_gui_core/issues/14>`_)
* fix help provider
* fix container being closable even when perspective is locked (`#20 <https://github.com/ros-visualization/qt_gui_core/issues/20>`_)
* fix search path of theme icons for OS X (`#17 <https://github.com/ros-visualization/qt_gui_core/issues/17>`_)

0.2.15 (2013-04-02)
-------------------
* revert changes to help_provider from 0.2.13

0.2.14 (2013-03-28 22:42)
-------------------------

0.2.13 (2013-03-28 18:08)
-------------------------
* modify help_provider
* fix menu bar visibility on OS X

0.2.12 (2013-01-17)
-------------------
* fix when dbus is available but no session bus (`#9 <https://github.com/ros-visualization/qt_gui_core/issues/9>`_)

0.2.11 (2013-01-13)
-------------------

0.2.10 (2013-01-11)
-------------------
* add option -t option to keep windows always on top
* enable plugins to provide their arguments for the command line

0.2.9 (2012-12-21)
------------------
* first public release for Groovy
