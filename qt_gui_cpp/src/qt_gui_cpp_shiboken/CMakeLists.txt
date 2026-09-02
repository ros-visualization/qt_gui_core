
# Cannot use shiboken because of bugs in Debian and Ubuntu
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1131536
# https://bugs.launchpad.net/ubuntu/+source/pyside6/+bug/2146611
return()

find_package(Qt6Widgets REQUIRED)

set(qt_gui_cpp_shiboken_QT_COMPONENTS
  QtCore
  QtGui
  QtWidgets
)

set(qt_gui_cpp_shiboken_SRCS
  libqt_gui_cpp_shiboken/libqt_gui_cpp_shiboken_module_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_compositepluginprovider_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_genericproxy_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_plugin_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_pluginbridge_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_plugincontext_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_plugindescriptor_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_pluginprovider_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_recursivepluginprovider_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_rospluginlibpluginprovider_forpluginproviders_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_rospluginlibpluginprovider_forplugins_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_settings_wrapper.cpp
  libqt_gui_cpp_shiboken/qt_gui_cpp_wrapper.cpp
)

set(qt_gui_cpp_INCLUDE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../../include)
set(qt_gui_cpp_HDRS
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/composite_plugin_provider.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/generic_proxy.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/plugin.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/plugin_bridge.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/plugin_context.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/plugin_descriptor.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/plugin_provider.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/recursive_plugin_provider.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/ros_pluginlib_plugin_provider.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/ros_pluginlib_plugin_provider_for_plugin_providers.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/ros_pluginlib_plugin_provider_for_plugins.hpp
  ${qt_gui_cpp_INCLUDE_PATH}/qt_gui_cpp/settings.hpp
)
ament_get_recursive_properties(deps_include_dirs _ ${TinyXML2_TARGETS} ${pluginlib_TARGETS})
list(APPEND qt_gui_cpp_INCLUDE_PATH ${deps_include_dirs})

find_package(python_qt_binding REQUIRED)
list(APPEND qt_gui_cpp_BINDINGS "shiboken")
set(qt_gui_cpp_BINDINGS "${qt_gui_cpp_BINDINGS}" PARENT_SCOPE)
# Find required packages
find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(Shiboken6Tools REQUIRED)

set(shiboken_extra_options_str "")
foreach(dir ${class_loader_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS} ${rcutils_INCLUDE_DIRS} ${rcpputils_INCLUDE_DIRS})
  list(APPEND shiboken_extra_options_str "-I\"${dir}\"")
endforeach()

message(shiboken_extra_options_str ${shiboken_extra_options_str})

# Create Python bindings using Shiboken6Tools function
shiboken_generator_create_binding(
    EXTENSION_TARGET libqt_gui_cpp_shiboken
    GENERATED_SOURCES ${qt_gui_cpp_shiboken_SRCS}
    HEADERS "${CMAKE_CURRENT_SOURCE_DIR}/global.h"
    TYPESYSTEM_FILE ${CMAKE_CURRENT_SOURCE_DIR}/typesystem.xml
    LIBRARY_TARGET qt_gui_cpp
    SHIBOKEN_EXTRA_OPTIONS
      ${shiboken_extra_options_str}
      -I${CMAKE_CURRENT_SOURCE_DIR}/../../include
    QT_MODULES Core Gui Widgets
)
install(TARGETS libqt_gui_cpp_shiboken
  DESTINATION ${PYTHON_INSTALL_DIR}/${PROJECT_NAME})

