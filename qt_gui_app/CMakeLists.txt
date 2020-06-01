cmake_minimum_required(VERSION 3.0.2)
project(qt_gui_app)

find_package(catkin REQUIRED)
catkin_package()

catkin_python_setup()

catkin_install_python(PROGRAMS scripts/qt_gui_app
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
