^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package qt_gui_cpp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.4.2 (2020-07-24)
------------------
* quiet upstream Qt5 warnings (`#210 <https://github.com/ros-visualization/qt_gui_core/issues/210>`_) (`#229 <https://github.com/ros-visualization/qt_gui_core/issues/229>`_)
* declare private assignment operator for SIP (`#226 <https://github.com/ros-visualization/qt_gui_core/issues/226>`_)

0.4.1 (2020-05-28)
------------------
* use setuptools instead of distutils (`#209 <https://github.com/ros-visualization/qt_gui_core/issues/209>`_)

0.4.0 (2020-02-28)
------------------
* fix namespace in typesystem.xml (`#201 <https://github.com/ros-visualization/qt_gui_core/issues/201>`_)

0.3.17 (2020-02-28)
-------------------
* bump CMake minimum version to avoid CMP0048 warning (`#206 <https://github.com/ros-visualization/qt_gui_core/issues/206>`_)

0.3.16 (2019-12-04)
-------------------

0.3.15 (2019-10-23)
-------------------
* rework for Windows linkage (`#188 <https://github.com/ros-visualization/qt_gui_core/issues/188>`_)

0.3.14 (2019-10-03)
-------------------
* fix compile regression on armhf (`#187 <https://github.com/ros-visualization/qt_gui_core/issues/187>`_, regression from 0.3.12)

0.3.13 (2019-09-30)
-------------------

0.3.12 (2019-09-30)
-------------------
* [Windows] Add missing DLL exports for qt_gui_cpp (`#170 <https://github.com/ros-visualization/qt_gui_core/issues/170>`_)
* cherry-pick windows port from crystal-devel (`#173 <https://github.com/ros-visualization/qt_gui_core/issues/173>`_)
* remove obsolete maintainer (`#160 <https://github.com/ros-visualization/qt_gui_core/issues/160>`_)
* changes for flake8 and ROS2 compatible style changes (`#130 <https://github.com/ros-visualization/qt_gui_core/issues/130>`_)
* autopep8 (`#123 <https://github.com/ros-visualization/qt_gui_core/issues/123>`_)

0.3.11 (2018-08-29)
-------------------

0.3.10 (2018-08-05)
-------------------

0.3.9 (2018-08-03)
------------------
* change included pluginlib header to avoid deprecation warning (`#114 <https://github.com/ros-visualization/qt_gui_core/issues/114>`_)

0.3.8 (2017-11-03)
------------------

0.3.7 (2017-10-25)
------------------

0.3.6 (2017-08-03)
------------------
* add missing run_depend on TinyXML (`#100 <https://github.com/ros-visualization/qt_gui_core/issues/100>`_)
* add TinyXML to target_link_libraries (`#99 <https://github.com/ros-visualization/qt_gui_core/issues/99>`_)

0.3.5 (2017-07-27)
------------------
* find and depend on tinyxml, add missing tinyxml include (`#96 <https://github.com/ros-visualization/qt_gui_core/issues/96>`_, `#97 <https://github.com/ros-visualization/qt_gui_core/issues/97>`_)
* fix relative import for Python3 (`#89 <https://github.com/ros-visualization/qt_gui_core/pull/89>`_)

0.3.4 (2017-01-24)
------------------

0.3.3 (2016-09-19)
------------------

0.3.2 (2016-04-21)
------------------

0.3.1 (2016-04-18)
------------------
* more fixes for shiboken 2
* add missing Qt include directories

0.3.0 (2016-04-01)
------------------
* switch to Qt5 (`#64 <https://github.com/ros-visualization/qt_gui_core/pull/64>`_)

0.2.30 (2016-03-30)
-------------------

0.2.29 (2015-09-19)
-------------------

0.2.28 (2015-06-08)
-------------------

0.2.27 (2015-04-29)
-------------------

0.2.26 (2014-08-18)
-------------------

0.2.25 (2014-07-10)
-------------------
* fix finding specific version of PythonLibs with CMake 3 (`#45 <https://github.com/ros-visualization/qt_gui_core/issues/45>`_)

0.2.24 (2014-05-21)
-------------------

0.2.23 (2014-05-07)
-------------------

0.2.22 (2014-03-04)
-------------------
* add shutdown notification for plugin providers (`#39 <https://github.com/ros-visualization/qt_gui_core/issues/39>`_)

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
