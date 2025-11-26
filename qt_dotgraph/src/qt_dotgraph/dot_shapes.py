# Copyright (c) 2017, Open Source Robotics Foundation, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from python_qt_binding.QtCore import QRectF
from python_qt_binding.QtWidgets import QAbstractGraphicsShapeItem


class QGraphicsBox3dItem(QAbstractGraphicsShapeItem):

    def __init__(self, bounding_box):
        super(QGraphicsBox3dItem, self).__init__()
        self._bounding_box = bounding_box

    def boundingRect(self):
        return self._bounding_box

    def paint(self, painter, option, widget):
        # Main rectangle
        rectangle = QRectF(self._bounding_box.topLeft().x(),
                           self._bounding_box.topLeft().y() + self._bounding_box.height() * 0.1,
                           self._bounding_box.width() - self._bounding_box.height() * 0.1,
                           self._bounding_box.height() - self._bounding_box.height() * 0.1)
        painter.drawRect(rectangle)
        # Top line
        painter.drawLine(int(rectangle.topLeft().x() + self._bounding_box.height() * 0.1),
                         int(self._bounding_box.topLeft().y()),
                         int(self._bounding_box.topRight().x()),
                         int(self._bounding_box.topRight().y()))
        # Top left corner
        painter.drawLine(int(rectangle.topLeft().x() + self._bounding_box.height() * 0.1),
                         int(self._bounding_box.topLeft().y()),
                         int(self._bounding_box.topLeft().x() + 1),
                         int(rectangle.topLeft().y()))
        # Top right corner
        painter.drawLine(int(self._bounding_box.topRight().x()),
                         int(self._bounding_box.topRight().y()),
                         int(rectangle.topRight().x()),
                         int(rectangle.topRight().y()))
        # Bottom right corner
        painter.drawLine(int(rectangle.bottomRight().x() + 1),
                         int(rectangle.bottomRight().y() - 1),
                         int(self._bounding_box.bottomRight().x()),
                         int(rectangle.bottomRight().y() - self._bounding_box.height() * 0.1))
        # Right line
        painter.drawLine(int(self._bounding_box.topRight().x()),
                         int(self._bounding_box.topRight().y()),
                         int(self._bounding_box.topRight().x()),
                         int(self._bounding_box.bottomRight().y()
                             - self._bounding_box.height() * 0.1))
