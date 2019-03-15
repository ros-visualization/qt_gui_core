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
