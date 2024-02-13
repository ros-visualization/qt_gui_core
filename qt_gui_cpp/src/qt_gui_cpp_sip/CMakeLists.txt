set(qt_gui_cpp_HDRS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../include/qt_gui_cpp)
set(qt_gui_cpp_sip_DEPENDENT_FILES
  composite_plugin_provider.sip
  generic_proxy.sip
  plugin.sip
  plugin_bridge.sip
  plugin_context.sip
  plugin_descriptor.sip
  plugin_provider.sip
  recursive_plugin_provider.sip
  qt_gui_cpp.sip
  ros_pluginlib_plugin_provider_for_plugin_providers.sip
  ros_pluginlib_plugin_provider_for_plugins.sip
  settings.sip
  ${qt_gui_cpp_HDRS_DIR}/composite_plugin_provider.h
  ${qt_gui_cpp_HDRS_DIR}/generic_proxy.h
  ${qt_gui_cpp_HDRS_DIR}/plugin.h
  ${qt_gui_cpp_HDRS_DIR}/plugin_bridge.h
  ${qt_gui_cpp_HDRS_DIR}/plugin_context.h
  ${qt_gui_cpp_HDRS_DIR}/plugin_descriptor.h
  ${qt_gui_cpp_HDRS_DIR}/plugin_provider.h
  ${qt_gui_cpp_HDRS_DIR}/recursive_plugin_provider.h
  ${qt_gui_cpp_HDRS_DIR}/ros_pluginlib_plugin_provider.h
  ${qt_gui_cpp_HDRS_DIR}/ros_pluginlib_plugin_provider_for_plugin_providers.h
  ${qt_gui_cpp_HDRS_DIR}/ros_pluginlib_plugin_provider_for_plugins.h
  ${qt_gui_cpp_HDRS_DIR}/settings.h
)

# maintain context for different named target
set(qt_gui_cpp_sip_INCLUDE_DIRS ${qt_gui_cpp_INCLUDE_DIRS} "${CMAKE_CURRENT_SOURCE_DIR}/../../include")
set(qt_gui_cpp_sip_LIBRARY_DIRS ${qt_gui_cpp_LIBRARY_DIRS} lib)
set(qt_gui_cpp_sip_LDFLAGS_OTHER ${qt_gui_cpp_LDFLAGS_OTHER})

ament_get_recursive_properties(deps_include_dirs deps_libraries ${pluginlib_TARGETS})
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
  Python3::Python
  qt_gui_cpp
)

# sip needs libraries to have resolved paths and cannot link to cmake targets
foreach(_lib_name ${_qt_gui_cpp_sip_LIBRARIES})
  if(TARGET ${_lib_name})
    # Use a nifty cmake generator expression to resolve the target location
    list(APPEND qt_gui_cpp_sip_LIBRARIES $<TARGET_FILE:${_lib_name}>)
  else()
    # This library should work as is
    list(APPEND qt_gui_cpp_sip_LIBRARIES ${_lib_name})
  endif()
endforeach()

find_package(python_qt_binding REQUIRED)
include(${python_qt_binding_DIR}/sip_helper.cmake)

ament_export_dependencies(pluginlib)
include_directories(${PROJECT_NAME} ${qt_gui_cpp_INCLUDE_DIRECTORIES} ${deps_include_dirs})

# The include directories used by build_sip_binding are different than the one set in include directories
set(qt_gui_cpp_sip_INCLUDE_DIRS ${qt_gui_cpp_sip_INCLUDE_DIRS} ${deps_include_dirs})

if(sip_helper_FOUND)
  list(APPEND qt_gui_cpp_BINDINGS "sip")
  set(qt_gui_cpp_BINDINGS "${qt_gui_cpp_BINDINGS}" PARENT_SCOPE)

  build_sip_binding(qt_gui_cpp_sip qt_gui_cpp.sip
    SOURCE_DIR ${PROJECT_SOURCE_DIR}/src/qt_gui_cpp_sip
    LIBRARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS ${qt_gui_cpp_sip_DEPENDENT_FILES}
    DEPENDENCIES qt_gui_cpp
  )

  if(APPLE)
    set(LIBQT_GUI_CPP_SIP_SUFFIX .so)
  elseif(WIN32)
    set(LIBQT_GUI_CPP_SIP_SUFFIX .pyd)
  else()
    set(LIBQT_GUI_CPP_SIP_SUFFIX ${CMAKE_SHARED_LIBRARY_SUFFIX})
  endif()

  install(FILES ${CMAKE_CURRENT_BINARY_DIR}/libqt_gui_cpp_sip${LIBQT_GUI_CPP_SIP_SUFFIX}
      DESTINATION ${PYTHON_INSTALL_DIR}/${PROJECT_NAME})
endif()
