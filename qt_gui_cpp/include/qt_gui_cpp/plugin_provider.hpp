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

#ifndef QT_GUI_CPP__PLUGIN_PROVIDER_HPP_
#define QT_GUI_CPP__PLUGIN_PROVIDER_HPP_

#include "plugin.hpp"
#include "plugin_context.hpp"
#include "plugin_descriptor.hpp"

#include <QList>
#include <QMultiMap>
#include <QString>

namespace qt_gui_cpp
{

class PluginProvider
{
public:
  PluginProvider();

  virtual ~PluginProvider();

  virtual QMultiMap<QString, QString> discover(QObject * discovery_data);

  /**
   * @attention Ownership of returned PluginDescriptor's is transfered to the caller
   */
  virtual QList<PluginDescriptor *> discover_descriptors(QObject * discovery_data);

  virtual void * load(const QString & plugin_id, PluginContext * plugin_context);

  virtual Plugin * load_plugin(const QString & plugin_id, PluginContext * plugin_context);

  virtual void unload(void * plugin_instance);

  virtual void unload_plugin(Plugin * plugin_instance);

  virtual void shutdown();
};
}  // namespace qt_gui_cpp

#endif  // QT_GUI_CPP__PLUGIN_PROVIDER_HPP_
