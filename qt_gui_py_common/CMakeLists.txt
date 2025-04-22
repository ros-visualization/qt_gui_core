cmake_minimum_required(VERSION 3.5)
project(qt_gui_py_common)

find_package(catkin REQUIRED)
catkin_package()

catkin_python_setup()

install(DIRECTORY resource
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
