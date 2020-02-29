cmake_minimum_required(VERSION 3.0.2)
project(qt_gui_cpp)

find_package(catkin REQUIRED COMPONENTS cmake_modules pluginlib)
find_package(Boost REQUIRED COMPONENTS filesystem system)
find_package(TinyXML REQUIRED)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS pluginlib
  CFG_EXTRAS ${PROJECT_NAME}-extras.cmake
  DEPENDS Boost TinyXML
)

catkin_python_setup()

include_directories(include ${catkin_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS} ${TinyXML_INCLUDE_DIRS})

add_subdirectory(src)

install(DIRECTORY include/qt_gui_cpp/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})
install(FILES plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
