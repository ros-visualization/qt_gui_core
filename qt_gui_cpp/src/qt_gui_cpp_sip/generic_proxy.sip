%Module(name=qt_gui_cpp_sip, use_limited_api=True)

namespace qt_gui_cpp
{

class GenericProxy
{
%TypeHeaderCode
#include <QObject>
#include <qt_gui_cpp/generic_proxy.hpp>
%End

public:

  GenericProxy(QObject* obj = 0);

};

};
