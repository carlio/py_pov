# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

#import os
import unittest
#import difflib
#import copy
from logging import *

from pov.atmeff.Fog import Fog
from pov.atmeff.SkySphere import SkySphere
from pov.texture.Pigment import Pigment
from pov.basic.Color import Color
from pov.basic.Vector import Vector


class FogTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Fog(Color(rgb=Vector(100, 100, 100)))

    def test_creation(self):
        self.assertIsInstance(self.SUT, Fog)


class SkySphereTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = SkySphere(Pigment())

    def test_creation(self):
        self.assertIsInstance(self.SUT, SkySphere)
