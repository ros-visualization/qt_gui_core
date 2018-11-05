cmake_minimum_required(VERSION 3.5)
project(qt_gui_app)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

install(PROGRAMS scripts/qt_gui_app DESTINATION bin)

ament_package()
