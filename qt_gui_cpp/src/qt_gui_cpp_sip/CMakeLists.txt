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

find_library(class_loader_LIBRARY class_loader)
find_library(console_bridge_LIBRARY console_bridge)
find_library(TinyXML2_LIBRARY tinyxml2)

set(_qt_gui_cpp_sip_LIBRARIES
  ${pluginlib_LIBRARIES}
  ${PYTHON_LIBRARY}
  ${TinyXML2_LIBRARY}
  ${class_loader_LIBRARY}
  ${console_bridge_LIBRARY}
)

foreach(_library ${_qt_gui_cpp_sip_LIBRARIES})
  if (EXISTS ${_library})
    list(APPEND qt_gui_cpp_sip_LIBRARIES ${_library})
  else()
    message(STATUS "Library with path \"${_library}\" was supposed to be linked, but the path is poorly formed or it does not exist. Therefore it won't be found by sip so it will be ignored")
  endif()
endforeach()

# The qt_gui_cpp library does not exist yet, but it will be built before sip generation
list(APPEND qt_gui_cpp_sip_LIBRARIES "$<TARGET_FILE:qt_gui_cpp>")

if(CMAKE_COMPILER_IS_GNUCXX)
  # this is needed to use the experimental/filesystem on Linux, but cannot be passed with
  # ament_export_libraries() because it is not absolute and cannot be found with find_library
  list(APPEND qt_gui_cpp_sip_LIBRARIES stdc++fs)
endif()

set(qt_gui_cpp_INCLUDE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../../include ${pluginlib_INCLUDE_DIRS})

find_package(python_qt_binding REQUIRED)
include(${python_qt_binding_DIR}/sip_helper.cmake)

ament_export_dependencies(pluginlib)
include_directories(${PROJECT_NAME} ${qt_gui_cpp_INCLUDE_DIRECTORIES} ${pluginlib_INCLUDE_DIRS})

# The include directories used by build_sip_binding are different than the one set in include directories
set(qt_gui_cpp_sip_INCLUDE_DIRS ${qt_gui_cpp_sip_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS})

if(sip_helper_FOUND)
  list(APPEND qt_gui_cpp_BINDINGS "sip")
  set(qt_gui_cpp_BINDINGS "${qt_gui_cpp_BINDINGS}" PARENT_SCOPE)

  build_sip_binding(qt_gui_cpp_sip qt_gui_cpp.sip
    SOURCE_DIR ${PROJECT_SOURCE_DIR}/src/qt_gui_cpp_sip
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

  install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../../lib/libqt_gui_cpp_sip${LIBQT_GUI_CPP_SIP_SUFFIX}
      DESTINATION ${PYTHON_INSTALL_DIR}/${PROJECT_NAME})
endif()
