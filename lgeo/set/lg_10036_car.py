/*******************************************************************************
 Persistence of Vision Ray Tracer Scene Description File
 File: 10036-1_car.pov
 Vers: 3.6
 Desc: Lego Set "Pizza To Go" Subpart: car
 Link: www.peeron.com/inv/sets/10036-1
 Date: 04/2013
 Auth: Chocokiko
*******************************************************************************/

/*******************************************************************************
Parts List
----------

2348b   TrBlue  Glass for Hinge Car Roof 4 x 4 Sunroof with Ridges
2349    White   Hinge Car Roof 4 x 4 Sunroof
2357    White   Brick 2 x 2 Corner
2412b   Red     Tile 1 x 2 Grille with Groove
2412b   White   Tile 1 x 2 Grille with Groove
2436    White   Bracket 1 x 2 - 1 x 4
2441    Red Car Base 7 x 4 x 2/3
3003    Yellow  Brick 2 x 2
3004    White   Brick 1 x 2
3010    White   Brick 1 x 4
3020    White   Plate 2 x 4
3021    Red     Plate 2 x 3
3022    White   Plate 2 x 2
3024    White   Plate 1 x 1
3069b   Black   Tile 1 x 2 with Groove
3641    Black   Tyre
3710    White   Plate 1 x 4
3788    White   Car Mudguard 2 x 4
3823    TrLtBlu Windscreen 2 x 4 x 2
3829c01 OldGray Car Steering Stand and Wheel (Complete)
3853    White   Window 1 x 4 x 3
3856    White   Window 1 x 2 x 3 Shutter
4073    TrYello Plate 1 x 1 Round 1 Extra
4085c   White   Plate 1 x 1 with Clip Vertical - Type 3
4624    White   Wheel Centre Small
4625    White   Hinge Tile 1 x 4
4865    Black   Panel 1 x 2 x 1
821407  White   Sticker Sheet Town Pizzeria Pizza Logos
*******************************************************************************/


/*******************************************************************************
LGEO Disclaimer
Well, it is possible but not recommended. LGEO uses a different coordinate
system and scaling than LDRAW, so it may be pretty hard to build a model by
placing the parts by hand. In LGEO, for historic reasons Y axis is the depth
axis, and Z is the up axis, where also Z has switched sign to LDRAW Y axis.
Sorry for that, but my understanding of coordinate to this time was a flat
standard XY coordinate system with a third Z axis coming out of the plane.
Scaling is to real measurements, where 1 POV-Ray unit is 10mm. So 0.8 is 20 LDU
(width of a LEGO brick) and 0.96 is 24 LDU (height of a LEGO brick).
*******************************************************************************/

//Only load once
#ifndef(set_10036_1_car)
#declare set_10036_1_car = 1;

/*******************************************************************************
Includes
*******************************************************************************/
// ==== Standard POV-Ray Includes ====
#include "colors.inc"     // Standard Color definitions
// #include "textures.inc"   // Standard Texture definitions
// #include "functions.inc"  // internal functions usable in user defined functions

// ==== Additional Includes ====
// Don't have all of the following included at once, it'll cost memory and time
// to parse!
// --- general include files ---
// #include "arrays.inc"     // macros for manipulating arrays
// #include "chars.inc"      // A complete library of character objects, by Ken Maeno
// #include "consts.inc"     // Various constants and alias definitions
// #include "debug.inc"      // contains various macros for debugging scene files
// #include "logo.inc"       // The official POV-Ray Logo in various forms
// #include "math.inc"       // general math functions and macros
// #include "rad_def.inc"    // Some common radiosity settings
// #include "rand.inc"       // macros for generating random numbers
// #include "shapes.inc"     // macros for generating various shapes
// #include "shapes2.inc"    // some not built in basic shapes
// #include "shapesq.inc"    // Pre-defined quartic shapes
// #include "skies.inc"      // Ready defined sky spheres
// #include "strings.inc"    // macros for generating and manipulating text strings
// #include "sunpos.inc"     // macro for sun position on a given date, time, and location on earth
// #include "transforms.inc" // transformation macros

// --- textures ---
// #include "finish.inc"     // Some basic finishes
// #include "glass.inc"      // Glass textures/interiors
// #include "golds.inc"      // Gold textures
// #include "metals.inc"     // Metallic pigments, finishes, and textures
// #include "stones.inc"     // Binding include-file for STONES1 and STONES2
// #include "stones1.inc"    // Great stone-textures created by Mike Miller
// #include "stones2.inc"    // More, done by Dan Farmer and Paul Novak
// #include "woodmaps.inc"   // Basic wooden colormaps
// #include "woods.inc"      // Great wooden textures created by Dan Farmer and Paul Novak

// ==== LGEO Colors and Definitions ====
#include "lg_color.inc"
#include "lg_defs.inc"

// ==== LGEO fixed parts ====

// ==== LGEO parts ====
#include "lg_2348b.inc"
#include "lg_2349.inc"
#include "lg_2357.inc"
#include "lg_2412b.inc"
#include "lg_2436.inc"
#include "lg_2441.inc"
#include "lg_3003.inc"
#include "lg_3004.inc"
#include "lg_3010.inc"
#include "lg_3020.inc"
#include "lg_3021.inc"
#include "lg_3022.inc"
#include "lg_3024.inc"
#include "lg_3069b.inc"
#include "lg_3641.inc"
#include "lg_3788.inc"
#include "lg_3823.inc"
#include "lg_3829c01.inc"
#include "lg_3853.inc"
#include "lg_3856.inc"
#include "lg_4073.inc"
#include "lg_4085c"
#include "lg_4624.inc"
#include "lg_4625.inc"
#include "lg_4865.inc"
// 821407 Missing

// ==== Custom Includes ====
#include "custom_macros.inc"

// Offset X
#declare set_10036_1_car_nonmoving_ox= 0;
// Offset Y
#declare set_10036_1_car_nonmoving_oy= 0;
// Offset Z
#declare set_10036_1_car_nonmoving_oz= 0;
// Rotation X
#declare set_10036_1_car_nonmoving_rx= 0;
// Rotation Y
#declare set_10036_1_car_nonmoving_ry= 0;
// Rotation Z
#declare set_10036_1_car_nonmoving_rz= 0;
#declare set_10036_1_car_nonmoving= union {
    /*******************************************************************************
    Objects (Step 1)
    *******************************************************************************/
    // 2441 Red Car Base 7 x 4 x 2/3
    StdBrick(lg_2441 , lg_red,           0,   3*LGPH,         0,  -90,   0,   0)

    /*******************************************************************************
    Objects (Step 2)
    *******************************************************************************/
    // 3022    White   Plate 2 x 2
    StdBrick(lg_3022 , lg_white,  2.5*LGBW,   4*LGPH,         0,  -90,   0,   0)
    // 2412b   White   Tile 1 x 2 Grille with Groove
    StdBrick(lg_2412b, lg_white,  0.5*LGBW,   3*LGPH, -1.5*LGBW,  -90,  90,   0)
    StdBrick(lg_2412b, lg_white,  0.5*LGBW,   3*LGPH,  1.5*LGBW,  -90,  90,   0)

    /*******************************************************************************
    Objects (Step 3)
    *******************************************************************************/
    // 3022    White   Plate 2 x 2
    StdBrick(lg_3022 ,  lg_white, -2.5*LGBW,   4*LGPH,         0,  -90,   0,   0)
    // 3010    White   Brick 1 x 4
    StdBrick(lg_3010 ,  lg_white,    -1*LGBW,   5*LGPH,         0,  -90,   0,   0)

    /*******************************************************************************
    Objects (Step 4)
    *******************************************************************************/
    // 3003    Yellow  Brick 2 x 2
    StdBrick(lg_3003 , lg_yellow,  0.5*LGBW,   5*LGPH,         0,  -90,   0,   0)
    // 3788    White   Car Mudguard 2 x 4
    StdBrick(lg_3788 ,  lg_white,  2.5*LGBW,   6*LGPH,         0,  -90,   0,   0)

    /*******************************************************************************
    Objects (Step 5)
    *******************************************************************************/
    // 3788    White   Car Mudguard 2 x 4
    StdBrick(lg_3788 ,  lg_white, -2.5*LGBW,   6*LGPH,         0,  -90,   0,   0)
    // 3021    Red     Plate 2 x 3
    StdBrick(lg_3021 ,    lg_red,   -2*LGBW,   6*LGPH,         0,  -90,  90,   0)
    // 3024    White   Plate 1 x 1
    StdBrick(lg_3024 ,  lg_white,   -1*LGBW,   6*LGPH, -1.5*LGBW,  -90,   0,   0)
    // 4085c   White   Plate 1 x 1 with Clip Vertical - Type 3
    StdBrick(lg_4085c,  lg_white,   -1*LGBW,   6*LGPH,  1.5*LGBW,  -90,   0,   0)

    /*******************************************************************************
    Objects (Step 6)
    *******************************************************************************/
    // 2436    White   Bracket 1 x 2 - 1 x 4
    StdBrick(lg_2436 ,  lg_white,    3*LGBW,   6*LGPH,    0*LGBW,  -90,   0,   0)
    // 3020    White   Plate 2 x 4
    StdBrick(lg_3020 ,  lg_white, -1.5*LGBW,   7*LGPH,    0*LGBW,  -90,   0,   0)

    /*******************************************************************************
    Objects (Step 7)
    *******************************************************************************/
    // 4073    TrYello Plate 1 x 1 Round
    StdBrick(lg_4073 , lg_clear_yellow, 4.1*LGBW, 5*LGPH,  -1.5*LGBW,    0, 90,   0)
    StdBrick(lg_4073 , lg_clear_yellow, 4.1*LGBW, 5*LGPH,   1.5*LGBW,    0, 90,   0)
    // 2412b   Red     Tile 1 x 2 Grille with Groove
    StdBrick(lg_2412b, lg_red   ,  4.0*LGBW,   4.7*LGPH,    0*LGBW,  -90,   0,  -90)
    // 3069b   Black   Tile 1 x 2 with Groove
    StdBrick(lg_3069b, lg_black ,     -2*LGBW,   8*LGPH,    0*LGBW,  -90,  180,   0)
    // 4865    Black   Panel 1 x 2 x 1
    StdBrick(lg_4865 ,  lg_black,     -1*LGBW,  10*LGPH,    0*LGBW,  -90,  180,   0)

    /*******************************************************************************
    Objects (Step 8)
    *******************************************************************************/
    // 3004    White   Brick 1 x 2
    StdBrick(lg_3004 ,  lg_white,   -1.5*LGBW,  10*LGPH, -1.5*LGBW,  -90,  90,   0)
    StdBrick(lg_3004 ,  lg_white,   -1.5*LGBW,  10*LGPH,  1.5*LGBW,  -90,  90,   0)

    /*******************************************************************************
    Objects (Step 9)
    *******************************************************************************/
    // 3020    White   Plate 2 x 4
    StdBrick(lg_3020 ,  lg_white,   -1.5*LGBW,  11*LGPH,    0*LGBW,  -90,   0,   0)
    // 2357    White   Brick 2 x 2 Corner
    StdBrick(lg_2357 ,  lg_white,    3*LGBW,   9*LGPH, -1.5*LGBW,  -90,   0,   0)
    StdBrick(lg_2357 ,  lg_white,    3*LGBW,   9*LGPH,  1.5*LGBW,  -90, -90,   0)

    /*******************************************************************************
    Objects (Step 10)
    *******************************************************************************/
    // 3069b   Black   Tile 1 x 2 with Groove
    StdBrick(lg_3069b,  lg_black,    -2*LGBW,  12*LGPH,    0*LGBW,  -90, 180,   0)
    // 4865    Black   Panel 1 x 2 x 1
    StdBrick(lg_4865 ,  lg_black,    -1*LGBW,  14*LGPH,    0*LGBW,  -90, 180,   0)
    // 3823    TrLtBlu Windscreen 2 x 4 x 2
    StdBrick(lg_3823, lg_clear_cyan,  2*LGBW,  15*LGPH,    0*LGBW,  -90,   0,   0)

    /*******************************************************************************
    Objects (Step 11)
    *******************************************************************************/
    // 3853    White   Window 1 x 4 x 3
    StdBrick(lg_3853,   lg_white,    -3*LGBW,  15*LGPH,    0*LGBW,  -90,   180,   0)
    // 3004    White   Brick 1 x 2
    StdBrick(lg_3004,   lg_white,  -1.5*LGBW,  14*LGPH, -1.5*LGBW,  -90,  90,   0)
    StdBrick(lg_3004,   lg_white,  -1.5*LGBW,  14*LGPH,  1.5*LGBW,  -90,  90,   0)
    // 3010    White   Plate 1 x 4
    StdBrick(lg_3010,   lg_white,    -2*LGBW,  15*LGPH,    0*LGBW,  -90,   0,   0)

    /*******************************************************************************
    Objects (Step 12)
    *******************************************************************************/
    // 4625    White   Hinge Tile 1 x 4
    StdBrick(lg_4625,   lg_white,    -1*LGBW,  15*LGPH,    0*LGBW,  -90,   0,   0)

    /*******************************************************************************
    Objects (Step 13)
    *******************************************************************************/
    // 3020    White   Plate 2 x 4
    StdBrick(lg_3020,   lg_white,  -2.5*LGBW,  16*LGPH,    0*LGBW,  -90,   0,   0)
    // 4865    Black   Panel 1 x 2 x 1
    StdBrick(lg_4865,   lg_white,     2*LGBW,  19*LGPH,    0*LGBW,  -90, 180,   0)
    // TODO: Add Pizza design...

    split_union on
}

// 3829c01 OldGray Car Steering Stand and Wheel (Complete)
#declare set_10036_1_car_steering_wheel_ox= 2*LGBW;
#declare set_10036_1_car_steering_wheel_oy= 6*LGPH;
#declare set_10036_1_car_steering_wheel_oz= 0;
#declare set_10036_1_car_steering_wheel =
    StdBrick(lg_3829c01, lg_grey,      2*LGBW,   6*LGPH,    0*LGBW,  -90,   0,   0)

// 3856    White   Window 1 x 2 x 3 Shutter
#declare set_10036_1_car_schutter_l=
    StdBrick(lg_3856,   lg_white, -3.65*LGBW,  15*LGPH,   -2*LGBW,  -90, -90,   0)
#declare set_10036_1_car_schutter_l_ox= -3.65*LGBW;
#declare set_10036_1_car_schutter_l_oy= 15*LGPH;
#declare set_10036_1_car_schutter_l_oz= -2*LGBW;

#declare set_10036_1_car_schutter_r=
    StdBrick(lg_3856,   lg_white, -3.65*LGBW,  15*LGPH,    2*LGBW,  -90,  90,   0)
#declare set_10036_1_car_schutter_r_ox= -3.65*LGBW;
#declare set_10036_1_car_schutter_r_oy= 15*LGPH;
#declare set_10036_1_car_schutter_r_oz= 2*LGBW;

// 2349    White   Hinge Car Roof 4 x 4 Sunroof
#declare set_10036_1_car_sunroof=
    StdBrick(lg_2349,   lg_white,   0.5*LGBW,  16*LGPH,    0*LGBW,  -90,   0,   0)
#declare set_10036_1_car_sunroof_ox= 0.5*LGBW;
#declare set_10036_1_car_sunroof_oy= 16*LGPH;
#declare set_10036_1_car_sunroof_oz= 0;

// 2348b   TrBlue  Glass for Hinge Car Roof 4 x 4 Sunroof with Ridges
#declare set_10036_1_car_sunroof_glass=
    StdBrick(lg_2348b, lg_clear_cyan, 1.35*LGBW,15.5*LGPH,   0*LGBW,  -90,   0,   0)
#declare set_10036_1_car_sunroof_glass_ox= 1.35*LGBW;
#declare set_10036_1_car_sunroof_glass_oy= 15.5*LGPH;
#declare set_10036_1_car_sunroof_glass_oz= 0;

//4624    White   Wheel Centre Small
//3641    Black   Tyre
#declare set_10036_1_car_wheel_fr=
    union {
        UnchangedBrick(lg_4624, lg_white)
        UnchangedBrick(lg_3641, lg_black)

        rotate <-90, 90, 0>
        translate <-2.5*LGBW, 2.5*LGPH, -2*LGBW>
    }
#declare set_10036_1_car_wheel_fr_ox= -2.5*LGBW;
#declare set_10036_1_car_wheel_fr_oy=  2.5*LGPH;
#declare set_10036_1_car_wheel_fr_ox=   -2*LGBW;

#declare set_10036_1_car_wheel_fl=
    union {
        UnchangedBrick(lg_4624, lg_white)
        UnchangedBrick(lg_3641, lg_black)

        rotate <-90, 90, 0>
        translate <2.5*LGBW, 2.5*LGPH, -2*LGBW>
    }
#declare set_10036_1_car_wheel_fl_ox=  2.5*LGBW;
#declare set_10036_1_car_wheel_fl_oy=  2.5*LGPH;
#declare set_10036_1_car_wheel_fl_ox=   -2*LGBW;

#declare set_10036_1_car_wheel_rl =
    union {
        UnchangedBrick(lg_4624, lg_white)
        UnchangedBrick(lg_3641, lg_black)

        rotate <-90, -90, 0>
        translate <-2.5*LGBW, 2.5*LGPH, 2*LGBW>
    }
#declare set_10036_1_car_wheel_rl_ox= -2.5*LGBW;
#declare set_10036_1_car_wheel_rl_oy=  2.5*LGPH;
#declare set_10036_1_car_wheel_rl_ox=    2*LGBW;


#declare set_10036_1_car_wheel_rr=
    union {
        UnchangedBrick(lg_4624, lg_white)
        UnchangedBrick(lg_3641, lg_black)

        rotate <-90, -90, 0>
        translate <2.5*LGBW, 2.5*LGPH, 2*LGBW>
    }
#declare set_10036_1_car_wheel_rr_ox=  2.5*LGBW;
#declare set_10036_1_car_wheel_rr_oy=  2.5*LGPH;
#declare set_10036_1_car_wheel_rr_ox=    2*LGBW;



#end