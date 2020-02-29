cmake_minimum_required(VERSION 3.0.2)
project(qt_gui)

find_package(catkin REQUIRED)
catkin_package()

catkin_python_setup()

install(DIRECTORY resource
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
