cmake_minimum_required(VERSION 3.5)
project(qt_gui_cpp)

find_package(ament_cmake REQUIRED)
find_package(Boost REQUIRED COMPONENTS filesystem system)
find_package(tinyxml_vendor REQUIRED)
find_package(pluginlib REQUIRED)

ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR src/${PROJECT_NAME})

include_directories(include ${ament_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS} ${TinyXML_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS})

add_subdirectory(src)

install(DIRECTORY include/qt_gui_cpp/
  DESTINATION include)
install(FILES plugin.xml
  DESTINATION share)
install(
    DIRECTORY include
    DESTINATION include
  )

ament_export_dependencies(Boost)
ament_export_dependencies(TinyXML)
ament_export_dependencies(pluginlib)

ament_export_include_directories(include ${pluginlib_INCLUDE_DIRS})
ament_export_libraries(${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package(CONFIG_EXTRAS cmake/${PROJECT_NAME}-extras.cmake)
