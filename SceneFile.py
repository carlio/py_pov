"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


class SceneFile(list):
    """docstring for SceneFile"""
    def __init__(self, arg):
        super(SceneFile, self).__init__()
        self.arg = arg
