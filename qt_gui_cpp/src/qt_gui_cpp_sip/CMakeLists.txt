set(qt_gui_cpp_HDRS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../include/qt_gui_cpp)

set(qt_gui_cpp_sip "qt_gui_cpp.sip")
if(${qt_gui_cpp_USE_QT_MAJOR_VERSION} GREATER "5")
  set(qt_gui_cpp_sip "qt_gui_cpp_6.sip")
endif()

set(qt_gui_cpp_sip_DEPENDENT_FILES
  composite_plugin_provider.sip
  generic_proxy.sip
  plugin.sip
  plugin_bridge.sip
  plugin_context.sip
  plugin_descriptor.sip
  plugin_provider.sip
  recursive_plugin_provider.sip
  ${qt_gui_cpp_sip}
  ros_pluginlib_plugin_provider_for_plugin_providers.sip
  ros_pluginlib_plugin_provider_for_plugins.sip
  settings.sip
  ${qt_gui_cpp_HDRS_DIR}/composite_plugin_provider.hpp
  ${qt_gui_cpp_HDRS_DIR}/generic_proxy.hpp
  ${qt_gui_cpp_HDRS_DIR}/plugin.hpp
  ${qt_gui_cpp_HDRS_DIR}/plugin_bridge.hpp
  ${qt_gui_cpp_HDRS_DIR}/plugin_context.hpp
  ${qt_gui_cpp_HDRS_DIR}/plugin_descriptor.hpp
  ${qt_gui_cpp_HDRS_DIR}/plugin_provider.hpp
  ${qt_gui_cpp_HDRS_DIR}/recursive_plugin_provider.hpp
  ${qt_gui_cpp_HDRS_DIR}/ros_pluginlib_plugin_provider.hpp
  ${qt_gui_cpp_HDRS_DIR}/ros_pluginlib_plugin_provider_for_plugin_providers.hpp
  ${qt_gui_cpp_HDRS_DIR}/ros_pluginlib_plugin_provider_for_plugins.hpp
  ${qt_gui_cpp_HDRS_DIR}/settings.hpp
)

# maintain context for different named target
set(qt_gui_cpp_sip_INCLUDE_DIRS ${qt_gui_cpp_INCLUDE_DIRS} "${CMAKE_CURRENT_SOURCE_DIR}/../../include")
set(qt_gui_cpp_sip_LIBRARY_DIRS ${qt_gui_cpp_LIBRARY_DIRS} lib)
set(qt_gui_cpp_sip_LDFLAGS_OTHER ${qt_gui_cpp_LDFLAGS_OTHER})

ament_get_recursive_properties(deps_include_dirs deps_libraries pluginlib::pluginlib)
list(APPEND deps_include_dirs ${TinyXML2_INCLUDE_DIRS})
list(APPEND deps_libraries ${TinyXML2_LIBRARIES})

# By default, without the settings below, find_package(Python3) will attempt
# to find the newest python version it can, and additionally will find the
# most specific version.  For instance, on a system that has
# /usr/bin/python3.10, /usr/bin/python3.11, and /usr/bin/python3, it will find
# /usr/bin/python3.11, even if /usr/bin/python3 points to /usr/bin/python3.10.
# The behavior we want is to prefer the "system" installed version unless the
# user specifically tells us othewise through the Python3_EXECUTABLE hint.
# Setting CMP0094 to NEW means that the search will stop after the first
# python version is found.  Setting Python3_FIND_UNVERSIONED_NAMES means that
# the search will prefer /usr/bin/python3 over /usr/bin/python3.11.  And that
# latter functionality is only available in CMake 3.20 or later, so we need
# at least that version.
cmake_minimum_required(VERSION 3.20)
cmake_policy(SET CMP0094 NEW)
set(Python3_FIND_UNVERSIONED_NAMES FIRST)

find_package(Python3 REQUIRED COMPONENTS Development)

set(_qt_gui_cpp_sip_LIBRARIES
  ${deps_libraries}
  ${TinyXML2_LIBRARIES}
  ${pluginlib_TARGETS}
  Python3::Python
  qt_gui_cpp
)

find_package(python_qt_binding REQUIRED)
include(${python_qt_binding_DIR}/sip_helper.cmake)

ament_export_dependencies(pluginlib)

if(sip_helper_FOUND)
  list(APPEND qt_gui_cpp_BINDINGS "sip")
  set(qt_gui_cpp_BINDINGS "${qt_gui_cpp_BINDINGS}" PARENT_SCOPE)

  build_sip_binding(qt_gui_cpp_sip ${qt_gui_cpp_sip}
    SOURCE_DIR ${PROJECT_SOURCE_DIR}/src/qt_gui_cpp_sip
    LIBRARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS ${qt_gui_cpp_sip_DEPENDENT_FILES}
    DEPENDENCIES qt_gui_cpp ${deps_libraries}
  )
  # build_sip_binding prefixes the target with "lib"
  install(TARGETS libqt_gui_cpp_sip
    DESTINATION "${PYTHON_INSTALL_DIR}/${PROJECT_NAME}"
  )
endif()
