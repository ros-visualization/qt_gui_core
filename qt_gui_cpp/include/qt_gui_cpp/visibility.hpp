#ifndef QT_GUI_CPP__VISIBILITY_HPP_
#define QT_GUI_CPP__VISIBILITY_HPP_

#include <QtCore/qglobal.h>

// Export symbols when creating .dll and .lib, and import them when using .lib.
#if BINDINGS_BUILD
#    define BINDINGS_API Q_DECL_EXPORT
#else
#    define BINDINGS_API Q_DECL_IMPORT
#endif

#endif // QT_GUI_CPP__VISIBILITY_HPP_