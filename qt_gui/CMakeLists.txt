cmake_minimum_required(VERSION 3.20)
project(qt_gui)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR src/${PROJECT_NAME})

install(DIRECTORY resource
  DESTINATION share/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  find_package(ament_lint_auto REQUIRED)

  ament_add_pytest_test(plugin_manager test/test_plugin_manager.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src)

  # Disabling copyright test. The copyright used in this package does not conform to
  # ament's copyright tests
  set(ament_cmake_copyright_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
