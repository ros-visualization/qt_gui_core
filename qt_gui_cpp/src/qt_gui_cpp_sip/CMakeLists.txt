set(qt_gui_cpp_HDRS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../include/qt_gui_cpp)

set(qt_gui_cpp_sip "qt_gui_cpp.sip")
if(${QT_VERSION_MAJOR} GREATER "5")
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

set(qt_gui_cpp_sip_LIBRARIES
  ${TinyXML2_LIBRARIES}
  ${pluginlib_TARGETS}
  qt_gui_cpp
)

find_package(python_qt_binding REQUIRED)
include(${python_qt_binding_DIR}/sip_helper.cmake)

ament_export_dependencies(pluginlib)

if(sip_helper_FOUND)
  list(APPEND qt_gui_cpp_BINDINGS "sip")
  set(qt_gui_cpp_BINDINGS "${qt_gui_cpp_BINDINGS}" PARENT_SCOPE)

  build_sip_binding(qt_gui_cpp_sip qt_gui_cpp.sip
    SOURCE_DIR ${PROJECT_SOURCE_DIR}/src/qt_gui_cpp_sip
    LIBRARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS ${qt_gui_cpp_sip_DEPENDENT_FILES}
    DEPENDENCIES qt_gui_cpp ${deps_libraries}
  )
  install(TARGETS ${_library_name}
    DESTINATION "${PYTHON_INSTALL_DIR}/${PROJECT_NAME}"
  )
endif()
