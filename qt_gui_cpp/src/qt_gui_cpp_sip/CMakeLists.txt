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

# ugly hack to obtain path to shared sip_configure.py
string(REGEX REPLACE "^([^;]*;)*([^;]+/python_qt_binding)/include(;[^;]*)*$" "\\2" python_qt_binding_SOURCE_DIR "${qt_gui_cpp_INCLUDE_DIRS}")

# maintain context for different named target
set(qt_gui_cpp_sip_INCLUDE_DIRS ${qt_gui_cpp_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/../../include ${catkin_INCLUDE_DIRS})
set(qt_gui_cpp_sip_LIBRARIES ${qt_gui_cpp_LIBRARIES} ${PROJECT_NAME} ${catkin_LIBRARIES} ${Boost_LIBRARIES})
set(qt_gui_cpp_sip_LIBRARY_DIRS ${qt_gui_cpp_LIBRARY_DIRS} ${CATKIN_DEVEL_PREFIX}/lib)
set(qt_gui_cpp_sip_LDFLAGS_OTHER ${qt_gui_cpp_LDFLAGS_OTHER} -Wl,-rpath,${CATKIN_DEVEL_PREFIX}/lib)

find_package(python_qt_binding REQUIRED)
include(${python_qt_binding_EXTRAS_DIR}/sip_helper.cmake)

if(sip_helper_FOUND)
  list(APPEND qt_gui_cpp_BINDINGS "sip")
  set(qt_gui_cpp_BINDINGS "${qt_gui_cpp_BINDINGS}" PARENT_SCOPE)

  build_sip_binding(qt_gui_cpp_sip qt_gui_cpp.sip
    SIP_CONFIGURE ${python_qt_binding_EXTRAS_DIR}/sip_configure.py
    SOURCE_DIR ${PROJECT_SOURCE_DIR}/src/qt_gui_cpp_sip
    LIBRARY_DIR ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_PYTHON_DESTINATION}
    DEPENDS ${qt_gui_cpp_sip_DEPENDENT_FILES}
    DEPENDENCIES qt_gui_cpp
  )

  if(APPLE)
    set(LIBQT_GUI_CPP_SIP_SUFFIX .so)
  else()
    set(LIBQT_GUI_CPP_SIP_SUFFIX ${CMAKE_SHARED_LIBRARY_SUFFIX})
  endif()

  install(FILES ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_PYTHON_DESTINATION}/libqt_gui_cpp_sip${LIBQT_GUI_CPP_SIP_SUFFIX}
      DESTINATION ${CATKIN_PACKAGE_PYTHON_DESTINATION})
endif()
