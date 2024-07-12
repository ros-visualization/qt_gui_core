cmake_minimum_required(VERSION 3.12)
project(qt_gui_cpp)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
endif()

find_package(ament_cmake REQUIRED)

# set(CMAKE_SKIP_BUILD_RPATH FALSE)
# set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
# set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

if(WIN32)
  message(STATUS "${PROJECT_NAME} is not yet supported on Windows. Package will not be built.")
  ament_package()
  file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/plugin.xml"
    "<library path=\"src\"/>")
  install(FILES "${CMAKE_CURRENT_BINARY_DIR}/plugin.xml"
    DESTINATION share/${PROJECT_NAME})
  return()
endif()

find_package(pluginlib REQUIRED)
find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Widgets Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Widgets Core)
find_package(tinyxml2_vendor REQUIRED)
find_package(TinyXML2 REQUIRED)

ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR src/${PROJECT_NAME})

set(qt_gui_cpp_SRCS
  src/qt_gui_cpp/composite_plugin_provider.cpp
  src/qt_gui_cpp/generic_proxy.cpp
  src/qt_gui_cpp/plugin_bridge.cpp
  src/qt_gui_cpp/plugin_context.cpp
  src/qt_gui_cpp/plugin_descriptor.cpp
  src/qt_gui_cpp/plugin_provider.cpp
  src/qt_gui_cpp/recursive_plugin_provider.cpp
  src/qt_gui_cpp/settings.cpp
)

set(qt_gui_cpp_HDRS
  include/qt_gui_cpp/plugin.hpp
  include/qt_gui_cpp/plugin_bridge.hpp
  include/qt_gui_cpp/plugin_context.hpp
)

if (${QT_VERSION_MAJOR} GREATER "5")
  qt_standard_project_setup()
  qt_wrap_cpp(turtlesim_node_MOCS ${qt_gui_cpp_HDRS})
else()
  qt5_wrap_cpp(turtlesim_node_MOCS ${qt_gui_cpp_HDRS})
endif()

add_library(${PROJECT_NAME} SHARED ${qt_gui_cpp_SRCS} ${qt_gui_cpp_MOCS})
target_include_directories(${PROJECT_NAME} PUBLIC
  "$<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>"
  "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>")

target_link_libraries(${PROJECT_NAME}
  ${QT_QTCORE_LIBRARY}
  ${QT_QTGUI_LIBRARY}
  Qt${QT_VERSION_MAJOR}::Widgets
  pluginlib::pluginlib
  tinyxml2::tinyxml2)

add_subdirectory(src/qt_gui_cpp_shiboken)
add_subdirectory(src/qt_gui_cpp_sip)

# message(STATUS "Python binding generators: ${qt_gui_cpp_BINDINGS}")
# if(NOT qt_gui_cpp_BINDINGS)
#   message(FATAL_ERROR "No Python binding generator found.")
# endif()

install(FILES plugin.xml
  DESTINATION share/${PROJECT_NAME})

install(
  DIRECTORY include/
  DESTINATION include/${PROJECT_NAME}
)

ament_export_dependencies(pluginlib TinyXML2)
ament_export_targets(export_${PROJECT_NAME} HAS_LIBRARY_TARGET)

install(TARGETS ${PROJECT_NAME}
  EXPORT export_${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  find_package(ament_cmake_pytest REQUIRED)

  if(TARGET qt_gui_cpp_shiboken)
    ament_add_pytest_test(qt_gui_cpp_shiboken test/test_imports_shiboken.py
      APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
      TIMEOUT 90)
  endif()

  if(TARGET qt_gui_cpp_sip)
    ament_add_pytest_test(qt_gui_cpp_sip test/test_imports_sip.py
      APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
      TIMEOUT 90)
  endif()
endif()

ament_package(CONFIG_EXTRAS cmake/${PROJECT_NAME}-extras.cmake)
