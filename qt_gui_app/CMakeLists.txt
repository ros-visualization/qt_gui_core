cmake_minimum_required(VERSION 3.5)
project(qt_gui_app)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS scripts/qt_gui_app
  RUNTIME DESTINATION bin
)

ament_package()
