#include "plugin_provider.h"
#include "plugin.h"
#include "ros_pluginlib_plugin_provider.h"
#include "exports.h"

// Explicit instantiation with export declaration for Windows.
template class QT_GUI_CPP_DECL qt_gui_cpp::RosPluginlibPluginProvider<qt_gui_cpp::Plugin>;
template class QT_GUI_CPP_DECL qt_gui_cpp::RosPluginlibPluginProvider<qt_gui_cpp::PluginProvider>;
