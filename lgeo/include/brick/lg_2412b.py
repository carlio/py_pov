'''*****************************************************************************/
*                                                                             */
* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
*                                                                             */
* 19980319 Lutz Uhlmann                                                       */
* 20071101 Lutz Uhlmann moved from lg_2412 to lg_2412b                        */
*                                                                             */
* This file is in no way related to the LEGO(tm) Group.                       */
* It is provided for private non-commercial use only.                         */
*                                                                             */
* lg_2412b: Tile 1 x 2 Grille with Groove                                     */
*                                                                             */
*****************************************************************************'''

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Torus import Torus

from pov.object_modifier.Matrix import Matrix
from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object

from lgeo.include.common.lg_defs import *


def solid(LENGTH=2, WIDTH=1):
    return Union(
        Sphere(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
            Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE+0.04), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_WALL_WIDTH-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, (LG_WALL_WIDTH-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (2*LG_WALL_WIDTH+LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, (2*LG_WALL_WIDTH+LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (3*LG_WALL_WIDTH-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, (3*LG_WALL_WIDTH-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (4*LG_WALL_WIDTH+LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, (4*LG_WALL_WIDTH+LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, 5*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 5*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Difference(
            Union(
                Box(
                    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0.04),
                    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT)
                ),
                Box(
                    Vector(0, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
                    Vector(LENGTH*LG_BRICK_WIDTH, WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
                ),
                Box(
                    Vector(LG_CORNER_SPACE, 0, LG_CORNER_SPACE+0.04),
                    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, WIDTH*LG_BRICK_WIDTH, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
                ),
                Box(
                    Vector(0.04, 0.04, 0),
                    Vector((LENGTH*LG_BRICK_WIDTH-0.04), (WIDTH*LG_BRICK_WIDTH-0.04), 0.04+LG_E)
                )
            ),
            Union(
                Box(
                    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
                    Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, WIDTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT+LG_E)
                ),
                Box(
                    Vector(-LG_E, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
                    Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE)
                ),
                Box(
                    Vector(LENGTH*LG_BRICK_WIDTH+LG_E, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
                    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE)
                ),
                Box(
                    Vector(0, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
                    Vector(LENGTH*LG_BRICK_WIDTH, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
                ),
                Box(
                    Vector(0, LG_WALL_WIDTH, LG_PLATE_HEIGHT),
                    Vector(LENGTH*LG_BRICK_WIDTH, 2*LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
                ),
                Box(
                    Vector(-LG_E, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
                    Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE)
                ),
                Box(
                    Vector(LENGTH*LG_BRICK_WIDTH+LG_E, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
                    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE)
                ),
                Box(
                    Vector(0, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
                    Vector(LENGTH*LG_BRICK_WIDTH, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
                ),
                Box(
                    Vector(0, 3*LG_WALL_WIDTH, LG_PLATE_HEIGHT),
                    Vector(LENGTH*LG_BRICK_WIDTH, 4*LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
                )
            )
        ),
        Difference(
            Cylinder(
                Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH/2, LG_PLATE_INNER_HEIGHT+LG_E),
                Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH/2, 0),
                (LG_KNOB_INNER_RADIUS)
            ),
            Union(
                Box(
                    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_E),
                    Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, 2*LG_WALL_WIDTH, LG_PLATE_HEIGHT)
                ),
                Box(
                    Vector(LG_WALL_WIDTH, 3*LG_WALL_WIDTH, -LG_E),
                    Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, 4*LG_WALL_WIDTH, LG_PLATE_HEIGHT)
                ),
            ),
        ),
        Translate(Vector(-LG_BRICK_WIDTH, -0.5*LG_BRICK_WIDTH, -LG_PLATE_HEIGHT)),
        Rotate(Vector(0, 0, 90))
    )


'''
#declare lg_2412b_clear =
Merge(
 Sphere(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
  Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE+0.04), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE+0.04),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_WALL_WIDTH-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, (LG_WALL_WIDTH-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (2*LG_WALL_WIDTH+LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, (2*LG_WALL_WIDTH+LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (3*LG_WALL_WIDTH-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, (3*LG_WALL_WIDTH-LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (4*LG_WALL_WIDTH+LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, (4*LG_WALL_WIDTH+LG_CORNER_SPACE), (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, 5*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 5*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Difference(
  Merge(
   Box(
    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0.04),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT)
   ),
   Box(
    Vector(0, LG_CORNER_SPACE, LG_CORNER_SPACE+0.04),
    Vector(LENGTH*LG_BRICK_WIDTH, WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(LG_CORNER_SPACE, 0, LG_CORNER_SPACE+0.04),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, WIDTH*LG_BRICK_WIDTH, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(0.04, 0.04, 0),
    Vector((LENGTH*LG_BRICK_WIDTH-0.04), (WIDTH*LG_BRICK_WIDTH-0.04), 0.04+LG_E)
   ),
  ),
  Union(
   Box(
    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, WIDTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT+LG_E)
   ),
   Box(
    Vector(-LG_E, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
    Vector(LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(LENGTH*LG_BRICK_WIDTH+LG_E, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(0, LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
    Vector(LENGTH*LG_BRICK_WIDTH, 2*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(0, LG_WALL_WIDTH, LG_PLATE_HEIGHT),
    Vector(LENGTH*LG_BRICK_WIDTH, 2*LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
   ),
   Box(
    Vector(-LG_E, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
    Vector(LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(LENGTH*LG_BRICK_WIDTH+LG_E, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_INNER_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(0, 3*LG_WALL_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT+LG_E),
    Vector(LENGTH*LG_BRICK_WIDTH, 4*LG_WALL_WIDTH+LG_CORNER_SPACE, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(0, 3*LG_WALL_WIDTH, LG_PLATE_HEIGHT),
    Vector(LENGTH*LG_BRICK_WIDTH, 4*LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
   ),
  ),
 ),
 Difference(
  Cylinder(
   Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH/2, LG_PLATE_INNER_HEIGHT+LG_E),
   Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH/2, 0),
   (LG_KNOB_INNER_RADIUS)
  ),
  Union(
   Box(
    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_E),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, 2*LG_WALL_WIDTH, LG_PLATE_HEIGHT)
   ),
   Box(
    Vector(LG_WALL_WIDTH, 3*LG_WALL_WIDTH, -LG_E),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, 4*LG_WALL_WIDTH, LG_PLATE_HEIGHT)
   ),
  ),
 ),
 Translate(Vector(-LG_BRICK_WIDTH, -0.5*LG_BRICK_WIDTH, -LG_PLATE_HEIGHT)),
 Rotate(Vector(0, 0, 90))
),

#end
'''