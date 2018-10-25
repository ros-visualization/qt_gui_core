cmake_minimum_required(VERSION 3.5)
project(qt_dotgraph)

find_package(ament_cmake REQUIRED)

ament_python_install_package(${PROJECT_NAME}
        PACKAGE_DIR src/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
