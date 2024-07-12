namespace qt_gui_cpp
{

class RecursivePluginProvider
  : qt_gui_cpp::CompositePluginProvider
{
%TypeHeaderCode
#include <qt_gui_cpp/recursive_plugin_provider.hpp>
%End

public:

  RecursivePluginProvider(qt_gui_cpp::RosPluginlibPluginProvider_ForPluginProviders* plugin_provider);

  virtual ~RecursivePluginProvider();

  virtual QMultiMap<QString, QString> discover(QObject* discovery_data);

  virtual void shutdown();
};

};
