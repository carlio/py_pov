# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import *

from pov.basic.SceneItem import SceneItem
from pov.other.SdlSyntaxException import SdlSyntaxException


class Gradient(SceneItem):
    '''
        pigment {
            gradient <Orientation>
            [PIGMENT_MODIFIERS...]
        }
    '''

    def __init__(self, orientation):
        '''
            Create Gradient object

            @todo: Syntax checks
        '''
        super(Gradient, self).__init__('gradient', [orientation], [], [])

    def __str__(self):
        '''
            Generate PoV source code
        '''
        code = self._getLine(self.name + ' ' + str(self.args[0]))

        debug("Gradient.__str__(): %s\n%s" % (self.args[0], code))

        return code
