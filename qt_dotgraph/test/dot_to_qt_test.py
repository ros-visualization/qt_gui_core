#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2009, Willow Garage, Inc.
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

import unittest

from qt_dotgraph.dot_to_qt import DotToQtGenerator, get_unquoted
from python_qt_binding.QtWidgets import QApplication
import sys
import subprocess


def check_x_server():
    p = subprocess.Popen(sys.executable, stdin=subprocess.PIPE)
    p.stdin.write('from python_qt_binding.QtWidgets import QApplication\n')
    p.stdin.write('app = QApplication([])\n')
    p.stdin.close()
    p.communicate()

    print(p.returncode)

    return p.returncode == 0



class DotToQtGeneratorTest(unittest.TestCase):

    DOT_CODE = '''
    digraph graph_name {
        graph [bb="0,0,154,108",
            rank=same
        ];
        node [label="\N"];
        subgraph cluster_foo {
            graph [bb="1,1,100,101",
                label=cluster_foo
            ];
        }
        foo	 [height=0.5,
            label=foo,
            pos="77,90",
            shape=box,
            width=0.75];
        bar	 [height=0.5,
            label=barbarbarbarbarbarbarbar,
            pos="77,18",
            shape=box,
            width=2.25];
        foo -> bar	 [pos="e,77,36.104 77,71.697 77,63.983 77,54.712 77,46.112"];
    }
    '''

    _Q_APP = None

    def __init__(self, *args):
        super(DotToQtGeneratorTest, self).__init__(*args)
        # needed for creation of QtGraphic items in NodeItem.__init__
        if DotToQtGeneratorTest._Q_APP is None:
            if check_x_server():
                DotToQtGeneratorTest._Q_APP = QApplication([])

    def test_simple_integration(self):
        if DotToQtGeneratorTest._Q_APP is None:
            raise unittest.case.SkipTest

        (nodes, edges) = DotToQtGenerator().dotcode_to_qt_items(
            DotToQtGeneratorTest.DOT_CODE, 1)
        self.assertEqual(3, len(nodes))  # cluster_foo, foo and bar
        self.assertEqual(1, len(edges))  # foo -> bar

    def test_label_sizes(self):
        if DotToQtGeneratorTest._Q_APP is None:
            raise unittest.case.SkipTest

        (nodes, edges) = DotToQtGenerator().dotcode_to_qt_items(DotToQtGeneratorTest.DOT_CODE, 1)

        self.longMessage = True
        for name, node in nodes.items():
            shape_rect = node._graphics_item.sceneBoundingRect()
            label_rect = node._label.sceneBoundingRect()
            self.assertLess(
                label_rect.width(),
                shape_rect.width(),
                "Label text for '%s' is wider than surrounding shape." % name)
            self.assertLess(
                label_rect.height(),
                shape_rect.height(),
                "Label text for '%s' is higher than surrounding shape." % name)

    def test_unquoted(self):
        self.assertEqual("foo", get_unquoted({'bar': 'foo'}, 'bar'))
