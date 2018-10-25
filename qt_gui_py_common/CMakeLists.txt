cmake_minimum_required(VERSION 3.5)
project(qt_gui_py_common)

find_package(ament_cmake REQUIRED)

ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR src/${PROJECT_NAME})

install(DIRECTORY resource
  DESTINATION share)

install(TARGETS ${_library_name}
  DESTINATION "${PYTHON_INSTALL_DIR}/${PROJECT_NAME}"
)

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  ament_add_pytest_test(${PROJECT_NAME} test
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 90)
endif()

ament_package()
