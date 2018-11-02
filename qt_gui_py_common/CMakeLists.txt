cmake_minimum_required(VERSION 3.5)
project(qt_gui_py_common)

find_package(ament_cmake REQUIRED)

ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR src/${PROJECT_NAME})

install(DIRECTORY resource
  DESTINATION share/${PROJECT_NAME})

install(TARGETS ${_library_name}
  DESTINATION "${PYTHON_INSTALL_DIR}/${PROJECT_NAME}"
)

ament_package()
