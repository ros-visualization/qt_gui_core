/*
 * Copyright (c) 2011, Dirk Thomas, TU Darmstadt
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of the TU Darmstadt nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef QT_GUI_CPP__ROS_PLUGINLIB_PLUGIN_PROVIDER_HPP_
#define QT_GUI_CPP__ROS_PLUGINLIB_PLUGIN_PROVIDER_HPP_

#include <QCoreApplication>
#include <QEvent>
#include <QList>
#include <QMap>
#include <QObject>
#include <QString>

#include <tinyxml2.h>

#include <memory>
#include <string>
#include <type_traits>

#include "plugin.hpp"
#include "plugin_context.hpp"
#include "plugin_descriptor.hpp"
#include "plugin_provider.hpp"

#include <pluginlib/class_loader.hpp>

namespace qt_gui_cpp
{
// The method definitions live in ros_pluginlib_plugin_provider.cpp, which
// explicitly instantiates this template for the only two types in use:
// RosPluginlibPluginProvider<Plugin> (RosPluginlibPluginProvider_ForPlugins) and
// RosPluginlibPluginProvider<PluginProvider>
// (RosPluginlibPluginProvider_ForPluginProviders).
template<typename T>
class RosPluginlibPluginProvider
  : public QObject,
  public PluginProvider
{
public:
  static RosPluginlibPluginProvider<T> * create_instance(
    const QString & export_tag,
    const QString & base_class_type);

  RosPluginlibPluginProvider(const QString & export_tag, const QString & base_class_type);

  ~RosPluginlibPluginProvider() override;

  QMultiMap<QString, QString> discover(QObject * discovery_data) override;

  QList<PluginDescriptor *> discover_descriptors(QObject * discovery_data) override;

  void * load(const QString & plugin_id, PluginContext * plugin_context) override;

  Plugin * load_plugin(const QString & plugin_id, PluginContext * plugin_context) override;

  virtual T * load_explicit_type(const QString & plugin_id, PluginContext * plugin_context);

  void unload(void * instance) override;

  bool event(QEvent * e) override;

protected:
  virtual std::shared_ptr<T> create_plugin(
    const std::string & lookup_name,
    PluginContext * plugin_context = nullptr);

  virtual void init_plugin(
    const QString & plugin_id, PluginContext * plugin_context,
    Plugin * plugin);

private:
  template<typename TVersion>
  struct TinyXMLAPIChoice
  {
    template<
      // the function signature must use a template argument to trigger SFINAE
      typename TDoc,
      // T needs to be an explicit argument for std::enable_if to have a type
      typename TType = TVersion,
      // only enable for TinyXML versions >= 6
      typename = typename std::enable_if<std::is_same<TType, std::true_type>::value>::type
    >
    static void warningWithErrorStr(
      const std::string & manifest_path, const TDoc & doc,
      std::true_type * = nullptr)
    {
      qWarning("RosPluginlibPluginProvider::parseManifest() could not load manifest \"%s\" (%s)",
          manifest_path.c_str(), doc.ErrorStr());
    }
    template<
      typename TDoc,
      typename TType = TVersion,
      typename = typename std::enable_if<std::is_same<TType, std::false_type>::value>::type
    >
    static void warningWithErrorStr(
      const std::string & manifest_path, const TDoc & doc,
      std::false_type * = nullptr)
    {
      qWarning(
          "RosPluginlibPluginProvider::parseManifest() could not load manifest \"%s\" (%s, %s)",
          manifest_path.c_str(), doc.GetErrorStr1(), doc.GetErrorStr2());
    }
  };

  bool parseManifest(
    const std::string & lookup_name, const std::string & plugin_path,
    QString & label, QString & statustip, QString & icon, QString & icontype,
    PluginDescriptor * plugin_descriptor);

  void parseActionAttributes(
    tinyxml2::XMLElement * element, const std::string & plugin_path,
    QString & label, QString & statustip, QString & icon, QString & icontype);

  QString export_tag_;

  QString base_class_type_;

  int unload_libraries_event_;

  std::unique_ptr<pluginlib::ClassLoader<T>> class_loader_;

  QMap<void *, std::shared_ptr<T>> instances_;

  QList<std::shared_ptr<T>> libraries_to_unload_;
};
}  // namespace qt_gui_cpp

#endif  // QT_GUI_CPP__ROS_PLUGINLIB_PLUGIN_PROVIDER_HPP_
