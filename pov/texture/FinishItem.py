# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from ..basic import BlockObject
from ..basic import SceneItem


class FinishItem(SceneItem):
    """
        FINISH:
            finish { [FINISH_IDENTIFIER] [FINISH_ITEMS] }
        FINISH_ITEMS:
            [ambient COLOR] & [diffuse FLOAT] & [brilliance FLOAT] & [PHONG] & [SPECULAR] & [REFLECTION] & [IRID] & [crand FLOAT] & [conserve_energy [BOOL]]
        PHONG:
            phong FLOAT & [phong_size FLOAT] & [metallic [FLOAT]]
        SPECULAR:
            specular FLOAT & [roughness FLOAT] & [metallic [FLOAT]]
        REFLECTION:
            reflection COLOR [reflection_exponent FLOAT] |
            reflection { [COLOR,] COLOR [REFLECTION_ITEMS] }
        REFLECTION_ITEMS:
            [fresnel BOOL] & [falloff FLOAT] & [exponent FLOAT] & [metallic [FLOAT]]
            Must also use interior {ior FLOAT} in the object when fresnel is used.
        IRID:
            irid { F_AMOUNT [IRID_ITEMS] }
        IRID_ITEMS:
            [thickness FLOAT] & [turbulence FLOAT]
    """

    def __init__(self, name, *opts, **kwargs):
        """
            base class for finish items

            @TODO: constructor apidoc
            @TODO: Syntax checking
        """
        super(FinishItem, self).__init__(name, args=[], opts=[], **kwargs)
