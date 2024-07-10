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

#ifndef QT_GUI_CPP_SHIBOKEN__GLOBAL_H_
#define QT_GUI_CPP_SHIBOKEN__GLOBAL_H_

#ifndef NULL
#define NULL 0
#endif

#include <QtCore/QtCore>
#include <QtGui/QtGui>
#include <QtWidgets/QtWidgets>

#include <qt_gui_cpp/composite_plugin_provider.hpp>
#include <qt_gui_cpp/generic_proxy.hpp>
#include <qt_gui_cpp/plugin.hpp>
#include <qt_gui_cpp/plugin_bridge.hpp>
#include <qt_gui_cpp/plugin_context.hpp>
#include <qt_gui_cpp/plugin_descriptor.hpp>
#include <qt_gui_cpp/plugin_provider.hpp>
#include <qt_gui_cpp/recursive_plugin_provider.hpp>
#include <qt_gui_cpp/ros_pluginlib_plugin_provider.hpp>
#include <qt_gui_cpp/ros_pluginlib_plugin_provider_for_plugin_providers.hpp>
#include <qt_gui_cpp/ros_pluginlib_plugin_provider_for_plugins.hpp>
#include <qt_gui_cpp/settings.hpp>

#endif  // QT_GUI_CPP_SHIBOKEN__GLOBAL_H_
