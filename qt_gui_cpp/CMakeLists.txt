cmake_minimum_required(VERSION 3.5)
project(qt_gui_cpp)

find_package(ament_cmake REQUIRED)
find_package(pluginlib REQUIRED)
find_package(tinyxml_vendor REQUIRED)

ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR src/${PROJECT_NAME})

include_directories(include ${TinyXML_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS})

add_subdirectory(src)

install(FILES plugin.xml
  DESTINATION share)

install(
  DIRECTORY include
  DESTINATION include
)

ament_export_dependencies(pluginlib)
ament_export_include_directories(include)

ament_export_include_directories(include)
ament_export_libraries(${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  ament_add_pytest_test(${PROJECT_NAME} test
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 90)
endif()

ament_package(CONFIG_EXTRAS cmake/${PROJECT_NAME}-extras.cmake)
