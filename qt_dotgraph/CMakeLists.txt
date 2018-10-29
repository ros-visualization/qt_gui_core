cmake_minimum_required(VERSION 3.5)
project(qt_dotgraph)

find_package(ament_cmake REQUIRED)

ament_python_install_package(${PROJECT_NAME}
        PACKAGE_DIR src/${PROJECT_NAME})

if (CATKIN_ENABLE_TESTING)
  catkin_add_nosetests(test)
endif()

ament_package()
