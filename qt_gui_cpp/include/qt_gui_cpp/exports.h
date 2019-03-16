/*
 * Copyright (c) Microsoft Corporation. All rights reserved.
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

#ifndef qt_gui_cpp__EXPORTS_H
#define qt_gui_cpp__EXPORTS_H

/*
  Windows import/export and gnu http://gcc.gnu.org/wiki/Visibility
  macros.
 */
#if defined(_MSC_VER)
    #define QT_GUI_CPP_HELPER_IMPORT __declspec(dllimport)
    #define QT_GUI_CPP_HELPER_EXPORT __declspec(dllexport)
    #define QT_GUI_CPP_HELPER_LOCAL
#elif __GNUC__ >= 4
    #define QT_GUI_CPP_HELPER_IMPORT __attribute__ ((visibility("default")))
    #define QT_GUI_CPP_HELPER_EXPORT __attribute__ ((visibility("default")))
    #define QT_GUI_CPP_HELPER_LOCAL  __attribute__ ((visibility("hidden")))
#else
    #define QT_GUI_CPP_HELPER_IMPORT
    #define QT_GUI_CPP_HELPER_EXPORT
    #define QT_GUI_CPP_HELPER_LOCAL
#endif

#ifdef ROS_BUILD_SHARED_LIBS // ros is being built around shared libraries
  #ifdef qt_gui_cpp_EXPORTS // we are building a shared lib/dll
    #define QT_GUI_CPP_DECL QT_GUI_CPP_HELPER_EXPORT
  #else // we are using shared lib/dll
    #define QT_GUI_CPP_DECL QT_GUI_CPP_HELPER_IMPORT
  #endif
#else // ros is being built around static libraries
  #define QT_GUI_CPP_DECL
#endif

#endif
