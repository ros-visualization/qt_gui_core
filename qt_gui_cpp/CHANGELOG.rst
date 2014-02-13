^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package qt_gui_cpp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.2.21 (2014-02-12)
-------------------

0.2.20 (2014-01-19)
-------------------
* disable shiboken when version is detected which would segfault (`#35 <https://github.com/ros-visualization/qt_gui_core/issues/35>`_)

0.2.19 (2014-01-08)
-------------------
* use specific python version catkin has decided on
* fix sip bindings when paths contain spaces (`#33 <https://github.com/ros-visualization/qt_gui_core/issues/33>`_)

0.2.18 (2013-10-09)
-------------------
* improve startup time (`#28 <https://github.com/ros-visualization/qt_gui_core/issues/28>`_)
* disabled check for existance of library for cpp plugins
* fix build on OS X with new version of SIP (`#26 <https://github.com/ros-visualization/qt_gui_core/issues/26>`_)

0.2.17 (2013-08-21)
-------------------
* add PluginLoadError for know errors to avoid printing stacktraces (`ros-visualization/rqt#85 <https://github.com/ros-visualization/rqt/issues/85>`_)

0.2.16 (2013-06-06)
-------------------
* make plugin resources relative to plugin.xml (instead of package.xml) (`#16 <https://github.com/ros-visualization/qt_gui_core/issues/16>`_)
* fix help provider

0.2.15 (2013-04-02)
-------------------
* revert changes to help_provider from 0.2.13

0.2.14 (2013-03-28 22:42)
-------------------------

0.2.13 (2013-03-28 18:08)
-------------------------
* work around for broken QGenericReturnArgument constuctor with shiboken, make it build on Ubuntu precise (`ros-visualization/rqt#7 <https://github.com/ros-visualization/rqt/issues/7>`_)
* modify help_provider

0.2.12 (2013-01-17)
-------------------

0.2.11 (2013-01-13)
-------------------

0.2.10 (2013-01-11)
-------------------

0.2.9 (2012-12-21)
------------------
* first public release for Groovy
