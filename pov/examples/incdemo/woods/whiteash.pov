// Persistence Of Vision Raytracer version 3.5 sample file.
//
// -w320 -h240
// -w800 -h600 +a0.3

#include "colors.inc"
#include "woods.inc"
#include "whiteash.map"

camera {
   location <0, 10, -20>
   direction <0, 0,  3>
   right x*1.33
   look_at 1.5*y
}

light_source {<-50, 50, -1000> color Gray75}
light_source {< 50, 30, -20> color White}

background { color Gray30 }

#declare Stack =
union {
   sphere{<0, 4, 0>, 1}
   cone { -y,1, y, 0.5 translate 2*y }
   box {-1,1}
   no_shadow
}

object {
    Stack
    texture{
        pigment {
            P_WoodGrain3A
            color_map { M_WhiteAsh }
            rotate x*85
        }
    }
}
