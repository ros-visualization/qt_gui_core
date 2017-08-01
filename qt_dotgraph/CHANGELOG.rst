^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package qt_dotgraph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.3.5 (2017-07-27)
------------------
* avoid collision of topic nodes with / and \_ (`#95 <https://github.com/ros-visualization/qt_gui_core/pull/95>`_)
* small fixes for Python3 compatibility (`#88 <https://github.com/ros-visualization/qt_gui_core/pull/88>`_)
* remove color item added unintentionally (`#86 <https://github.com/ros-visualization/qt_gui_core/pull/86>`_)
* fix missing label coloring on hover (`#85 <https://github.com/ros-visualization/qt_gui_core/pull/85>`_)
* parse subgraphs recursively (`#72 <https://github.com/ros-visualization/qt_gui_core/issues/72>`_)

0.3.4 (2017-01-24)
------------------
* use Python 3 compatible syntax (`#81 <https://github.com/ros-visualization/qt_gui_core/pull/81>`_)
* fix label size in dot graphs (`#75 <https://github.com/ros-visualization/qt_gui_core/pull/75>`_)

0.3.3 (2016-09-19)
------------------
* work with newer pydot versions (`#70 <https://github.com/ros-visualization/qt_gui_core/pull/70>`_)
* make penwidth attribute optional

0.3.2 (2016-04-21)
------------------

0.3.1 (2016-04-18)
------------------
* fix imports with Qt 5

0.3.0 (2016-04-01)
------------------
* switch to Qt5 (`#64 <https://github.com/ros-visualization/qt_gui_core/pull/64>`_)

0.2.30 (2016-03-30)
-------------------
* use same color for arrows as for the edge (`#60 <https://github.com/ros-visualization/qt_gui_core/issues/60>`_)
* add ability to specify tooltips for nodes (`#61 <https://github.com/ros-visualization/qt_gui_core/pull/61>`_)

0.2.29 (2015-09-19)
-------------------

0.2.28 (2015-06-08)
-------------------
* skip subgraphs without a bounding box (`ros-visualization/rqt_common_plugins#321 <https://github.com/ros-visualization/rqt_common_plugins/issues/321>`_)

0.2.27 (2015-04-29)
-------------------
* add optional style argument for edges (`#51 <https://github.com/ros-visualization/qt_gui_core/pull/51>`_)
* fix tests (`#53 <https://github.com/ros-visualization/qt_gui_core/pull/53>`_)

0.2.26 (2014-08-18)
-------------------

0.2.25 (2014-07-10)
-------------------

0.2.24 (2014-05-21)
-------------------
* add work around for pydot bug in Saucy (`#42 <https://github.com/ros-visualization/qt_gui_core/issues/42>`_)
* fix regression 0.2.23 (`#41 <https://github.com/ros-visualization/qt_gui_core/issues/41>`_)

0.2.23 (2014-05-07)
-------------------
* add support for edge coloring and changing of pen width

0.2.22 (2014-03-04)
-------------------

0.2.21 (2014-02-12)
-------------------

0.2.20 (2014-01-19)
-------------------

0.2.19 (2014-01-08)
-------------------

0.2.18 (2013-10-09)
-------------------
* improve startup time (`#28 <https://github.com/ros-visualization/qt_gui_core/issues/28>`_)
* added kwarg for subgraphlabel
* change maintainer of qt_dotgraph (`#27 <https://github.com/ros-visualization/qt_gui_core/issues/27>`_)

0.2.17 (2013-08-21)
-------------------
* fix the name/label issue with pygraphviz

0.2.16 (2013-06-06)
-------------------

0.2.15 (2013-04-02)
-------------------

0.2.14 (2013-03-28 22:42)
-------------------------

0.2.13 (2013-03-28 18:08)
-------------------------

0.2.12 (2013-01-17)
-------------------

0.2.11 (2013-01-13)
-------------------

0.2.10 (2013-01-11)
-------------------
* skip subgraphs with empty bounding box
* use color for pydot subgraphs
* fix (not used) pygraphviz backend

0.2.9 (2012-12-21)
------------------
* first public release for Groovy
