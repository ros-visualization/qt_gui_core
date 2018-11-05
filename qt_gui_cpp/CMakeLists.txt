cmake_minimum_required(VERSION 3.5)
project(qt_gui_cpp)

find_package(ament_cmake REQUIRED)
find_package(pluginlib REQUIRED)
find_package(tinyxml_vendor REQUIRED)

ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR src/${PROJECT_NAME})

include_directories(include ${ament_INCLUDE_DIRS} ${TinyXML_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS})

add_subdirectory(src)

install(FILES plugin.xml
  DESTINATION share)
install(
    DIRECTORY include
    DESTINATION include
  )

ament_export_dependencies(pluginlib)
ament_export_dependencies(TinyXML)

ament_export_libraries(${PROJECT_NAME})

ament_package(CONFIG_EXTRAS cmake/${PROJECT_NAME}-extras.cmake)
