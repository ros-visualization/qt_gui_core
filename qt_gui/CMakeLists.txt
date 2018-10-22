cmake_minimum_required(VERSION 2.8.3)
project(qt_gui)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(DIRECTORY resource
  DESTINATION share/${PROJECT_NAME}/)
