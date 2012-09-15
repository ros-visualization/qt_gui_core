# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Dorian Scholz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from python_qt_binding.QtGui import QRadioButton, QVBoxLayout, QLabel, QWidget, QButtonGroup, QGroupBox

class ExclusiveOptionGroup(QGroupBox):
    
    def __init__(self, options, title='Exclusive Options', selected_index=None):
        super(ExclusiveOptionGroup, self).__init__()
        self.setTitle(title)
        self.setLayout(QVBoxLayout())
        self._button_group = QButtonGroup()
        self._button_group.setExclusive(True)
        self._options = options
        
        button_id = 0
        for option in self._options:
            button_id += 1
            
            radio_button = QRadioButton(option.get('title', 'option %d' % button_id))
            radio_button.setEnabled(option.get('enabled', True))
            radio_button.setChecked(option.get('selected', False) or (button_id - 1) == selected_index)
            radio_button.setToolTip(option.get('tooltip', ''))

            widget = QWidget()
            widget.setLayout(QVBoxLayout())
            widget.layout().addWidget(radio_button)
            if 'description' in option:
                widget.layout().addWidget(QLabel(option['description']))
            
            self._button_group.addButton(radio_button, button_id)
            self.layout().addWidget(widget)
            
    def get_settings(self):
        selected_index = self._button_group.checkedId() - 1 
        if selected_index >= 0:
            return {'selected_index': selected_index, 'selected_option': self._options[selected_index]}
        return {'selected_index': None, 'selected_option': None}
