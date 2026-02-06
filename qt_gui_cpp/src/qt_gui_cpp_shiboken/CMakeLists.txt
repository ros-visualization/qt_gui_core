# find_package(QTWidgets NAMES Qt6Widgets)
find_package(Qt6Widgets REQUIRED)

set(qt_gui_cpp_shiboken_QT_COMPONENTS
  QtCore
  QtGui
  QtWidgets
)

set(qt_gui_cpp_shiboken_SRCS
  qt_gui_cpp_shiboken/qt_gui_cpp_shiboken_module_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_compositepluginprovider_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_genericproxy_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_plugin_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_pluginbridge_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_plugincontext_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_plugindescriptor_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_pluginprovider_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_recursivepluginprovider_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_rospluginlibpluginprovider_forpluginproviders_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_rospluginlibpluginprovider_forplugins_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_settings_wrapper.cpp
  qt_gui_cpp_shiboken/qt_gui_cpp_wrapper.cpp
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
include(${python_qt_binding_DIR}/shiboken_helper.cmake)
ament_export_dependencies(pluginlib)
if(shiboken_helper_FOUND)
  # # if(Shiboken_VERSION VERSION_GREATER "1.1.1")
  # #   # shiboken 1.1.2 and higher will segfault until https://bugreports.qt-project.org/browse/PYSIDE-218 is fixed
  # #   message(WARNING "Shiboken version ${Shiboken_VERSION} would segfault when trying to process qt_gui_cpp "
  # #   "(see https://bugreports.qt-project.org/browse/PYSIDE-218)"
  # #   " Therefore shiboken bindings are being skipped.")
  # # else()
  #   list(APPEND qt_gui_cpp_BINDINGS "shiboken")
  #   set(qt_gui_cpp_BINDINGS "${qt_gui_cpp_BINDINGS}" PARENT_SCOPE)

  #   set(QT_INCLUDE_DIR "${Qt${QT_VERSION_MAJOR}Widgets_INCLUDE_DIRS}")
  #   # if(${QTWidgets_VERSION_MAJOR} GREATER "5")
  #     shiboken_generator6(libqt_gui_cpp global.h typesystem.xml ${PROJECT_SOURCE_DIR}/src/qt_gui_cpp_shiboken "${qt_gui_cpp_shiboken_SRCS}" "${qt_gui_cpp_HDRS}" "${qt_gui_cpp_INCLUDE_PATH}" "${CMAKE_CURRENT_BINARY_DIR}")
  #   # else()
  #     # shiboken_generator(libqt_gui_cpp global.h typesystem.xml ${PROJECT_SOURCE_DIR}/src/qt_gui_cpp_shiboken "${qt_gui_cpp_shiboken_SRCS}" "${qt_gui_cpp_HDRS}" "${qt_gui_cpp_INCLUDE_PATH}" "${CMAKE_CURRENT_BINARY_DIR}")
  #   # endif()

  #   shiboken_include_directories(qt_gui_cpp_shiboken "${qt_gui_cpp_shiboken_QT_COMPONENTS}")#:/home/ahcorde/ros2_rolling/qt6-env/lib/python3.12/site-packages/shiboken6/include)

  #   add_library(qt_gui_cpp_shiboken SHARED ${qt_gui_cpp_shiboken_SRCS})
  #   set_property(TARGET qt_gui_cpp_shiboken PROPERTY PREFIX "")
  #   target_compile_definitions(qt_gui_cpp_shiboken PRIVATE BINDINGS_BUILD)
  #   # target_include_directories(qt_gui_cpp_shiboken PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../../include)#:/home/ahcorde/ros2_rolling/qt6-env/lib/python3.12/site-packages/shiboken6/include)
  #   target_link_libraries(qt_gui_cpp_shiboken
  #     PUBLIC
  #       ${PROJECT_NAME}
  #       pluginlib::pluginlib
  #       tinyxml2::tinyxml2
  #     PRIVATE
  #       Qt6::Widgets
  #   )
  #   # shiboken_target_link_libraries(qt_gui_cpp_shiboken "${qt_gui_cpp_shiboken_QT_COMPONENTS}")

  #   install(TARGETS qt_gui_cpp_shiboken
  #     DESTINATION ${PYTHON_INSTALL_DIR}/${PROJECT_NAME})

#####################################################################################################################

    # Find required packages
    find_package(Python COMPONENTS Interpreter Development REQUIRED)
    # On RHEL and some other distros, Python wheels and site-packages may be installed under 'lib64'
    # instead of 'lib'. The FindPython CMake module may set Python_SITELIB to 'lib', which is incorrect
    # for these cases. To ensure compatibility, we override Python_SITELIB by querying Python directly.
    # This guarantees the correct site-packages path is used regardless of platform or Python build.
    execute_process(
        COMMAND ${Python_EXECUTABLE} -c
        "import site; print(next(p for p in site.getsitepackages() if 'site-packages' in p))"
        OUTPUT_VARIABLE Python_SITELIB
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )

    message("Python_SITELIB: ${Python_SITELIB}")

    list(APPEND CMAKE_PREFIX_PATH
        "${Python_SITELIB}/shiboken6_generator/lib/cmake"
    )
    find_package(Shiboken6Tools REQUIRED)

    # Get the relevant Qt include dirs, to pass them on to shiboken.
    get_property(QT_WIDGETS_INCLUDE_DIRS TARGET Qt6::Widgets PROPERTY INTERFACE_INCLUDE_DIRECTORIES)
    set(INCLUDES "")
    foreach(INCLUDE_DIR ${QT_WIDGETS_INCLUDE_DIRS})
        list(APPEND INCLUDES "-I${INCLUDE_DIR}")
    endforeach()
    list(APPEND INCLUDES "-I/home/ahcorde/ros2_rolling/install/include/pluginlib")

    list(APPEND SHIBOKEN_PYTHON_INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/../../include)
    # list(APPEND SHIBOKEN_PYTHON_INCLUDE_DIRS ${pluginlib_INCLUDE_DIRS})
    list(APPEND SHIBOKEN_PYTHON_INCLUDE_DIRS "/home/ahcorde/ros2_rolling/install/include/pluginlib")
    list(APPEND SHIBOKEN_PYTHON_LIBRARIES pluginlib::pluginlib)

    # We need to include the headers for the module bindings that we use.
    set(pyside_additional_includes "")
    foreach(INCLUDE_DIR ${pyside_include_dir})
        list(APPEND pyside_additional_includes "${INCLUDE_DIR}/QtCore")
        list(APPEND pyside_additional_includes "${INCLUDE_DIR}/QtGui")
        list(APPEND pyside_additional_includes "${INCLUDE_DIR}/QtWidgets")
    endforeach()
    list(APPEND pyside_additional_includes "/home/ahcorde/ros2_rolling/install/include/pluginlib")

    message("INCLUDES " ${INCLUDES})
    message("pyside_additional_includes " ${pyside_additional_includes})

    # add_library(qt_gui_cpp_shiboken SHARED ${qt_gui_cpp_shiboken_SRCS})
    # set_property(TARGET qt_gui_cpp_shiboken PROPERTY PREFIX "")
    # target_compile_definitions(qt_gui_cpp_shiboken PRIVATE BINDINGS_BUILD)
    # target_include_directories(qt_gui_cpp_shiboken PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../../include)
    # target_link_libraries(qt_gui_cpp_shiboken
    #   PUBLIC
    #     ${PROJECT_NAME}
    #     pluginlib::pluginlib
    #     tinyxml2::tinyxml2
    #   PRIVATE
    #     Qt6::Widgets
    # )

    # Create Python bindings using Shiboken6Tools function
    shiboken_generator_create_binding(
        EXTENSION_TARGET qt_gui_cpp_shiboken
        GENERATED_SOURCES ${qt_gui_cpp_shiboken_SRCS}
        HEADERS "${CMAKE_CURRENT_SOURCE_DIR}/global.h"
        TYPESYSTEM_FILE ${CMAKE_CURRENT_SOURCE_DIR}/typesystem.xml
        LIBRARY_TARGET qt_gui_cpp
        SHIBOKEN_EXTRA_OPTIONS
          -I"/home/ahcorde/ros2_rolling/install/include/pluginlib"
          -I"/home/ahcorde/ros2_rolling/install/include/class_loader"
          -I"/home/ahcorde/ros2_rolling/install/include/rcpputils"
          -I"/home/ahcorde/ros2_rolling/install/include/rcutils"
          -I"/home/ahcorde/ros2_rolling/install/include/ament_index_cpp"
        QT_MODULES Core Gui Widgets
    )
    install(TARGETS qt_gui_cpp_shiboken
      DESTINATION ${PYTHON_INSTALL_DIR}/${PROJECT_NAME})
endif()
