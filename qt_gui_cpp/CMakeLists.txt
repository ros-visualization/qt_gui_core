cmake_minimum_required(VERSION 2.8.3)
project(qt_gui_cpp)

find_package(catkin REQUIRED COMPONENTS pluginlib)
find_package(Boost REQUIRED COMPONENTS filesystem system)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS pluginlib
  DEPENDS Boost
)

catkin_python_setup()

include_directories(include ${catkin_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS})

add_subdirectory(src)

install(DIRECTORY include/qt_gui_cpp/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})
