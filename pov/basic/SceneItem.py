﻿# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013
based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from __future__ import nested_scopes
import os
from logging import *
from Vector import Vector
from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.other.IllegalStateException import IllegalStateException


class SceneItem(object):
    """
        Base class for POV objects.

        SCENE_ITEM:
            LANGUAGE_DIRECTIVES        |
            camera { CAMERA_ITEMS... } |
            OBJECTS                    |
            ATMOSPHERIC_EFFECTS        |
            global_settings { GLOBAL_ITEMS }
    """

    # All reserved identifiers for syntax checking purposes
    # @see: http://www.povray.org/documentation/view/3.6.1/226/
    __reserved_keywords = [
        'aa_level', 'aa_threshold', 'abs', 'absorption', 'accuracy', 'acos',
        'acosh', 'adaptive', 'adc_bailout', 'agate', 'agate_turb', 'all',
        'all_intersections', 'alpha', 'altitude', 'always_sample', 'ambient',
        'ambient_light', 'angle', 'aperture', 'append', 'arc_angle',
        'area_light', 'array', 'asc', 'ascii', 'asin', 'asinh', 'assumed_gamma',
        'atan', 'atan2', 'atanh', 'autostop', 'average',
        'b_spline', 'background', 'bezier_spline', 'bicubic_patch',
        'black_hole', 'blob', 'blue', 'blur_samples', 'bounded_by', 'box',
        'boxed', 'bozo', 'break', 'brick', 'brick_size', 'brightness',
        'brilliance', 'bump_map', 'bump_size', 'bumps',
        'camera', 'case', 'caustics', 'ceil', 'cells', 'charset', 'checker',
        'chr', 'circular', 'clipped_by', 'clock', 'clock_delta', 'clock_on',
        'collect', 'color', 'color_map', 'colour', 'colour_map', 'component',
        'composite', 'concat', 'cone', 'confidence', 'conic_sweep',
        'conserve_energy', 'contained_by', 'control0', 'control1', 'coords',
        'cos', 'cosh', 'count', 'crackle', 'crand', 'cube', 'cubic',
        'cubic_spline', 'cubic_wave', 'cutaway_textures', 'cylinder',
        'cylindrical',
        'debug', 'declare', 'default', 'defined', 'degrees', 'density',
        'density_file', 'density_map', 'dents', 'df3', 'difference', 'diffuse',
        'dimension_size', 'dimensions', 'direction', 'disc', 'dispersion',
        'dispersion_samples', 'dist_exp', 'distance', 'div', 'double_illuminate',
        'eccentricity', 'else', 'emission', 'end', 'error', 'error_bound',
        'evaluate', 'exp', 'expand_thresholds', 'exponent', 'exterior',
        'extinction',
        'face_indices', 'facets', 'fade_color', 'fade_colour', 'fade_distance',
        'fade_power', 'falloff', 'falloff_angle', 'false', 'fclose',
        'file_exists', 'filter', 'final_clock', 'final_frame', 'finish',
        'fisheye', 'flatness', 'flip', 'floor', 'focal_point', 'fog', 'fog_alt',
        'fog_offset', 'fog_type', 'fopen', 'form', 'frame_number', 'frequency',
        'fresnel', 'function',
        'gather', 'gif', 'global_lights', 'global_settings', 'gradient',
        'granite', 'gray', 'gray_threshold', 'green', 'height_field', 'hexagon',
        'hf_gray_16', 'hierarchy', 'hypercomplex', 'hollow', 'if', 'ifdef',
        'iff', 'ifndef', 'image_height', 'image_map', 'image_pattern',
        'image_width', 'include', 'initial_clock', 'initial_frame', 'inside',
        'inside_vector', 'int', 'interior', 'interior_texture', 'internal',
        'interpolate', 'intersection', 'intervals', 'inverse', 'ior', 'irid',
        'irid_wavelength', 'isosurface',
        'jitter', 'jpeg', 'julia', 'julia_fractal',
        'lambda', 'lathe', 'leopard', 'light_group', 'light_source',
        'linear_spline', 'linear_sweep', 'ln', 'load_file', 'local', 'location',
        'log', 'look_at', 'looks_like', 'low_error_factor',
        'macro', 'magnet', 'major_radius', 'mandel', 'map_type', 'marble',
        'material', 'material_map', 'matrix', 'max', 'max_extent',
        'max_gradient', 'max_intersections', 'max_iteration', 'max_sample',
        'max_trace', 'max_trace_level', 'media', 'media_attenuation',
        'media_interaction', 'merge', 'mesh', 'mesh2', 'metallic', 'method',
        'metric', 'min', 'min_extent', 'minimum_reuse', 'mod', 'mortar',
        'natural_spline', 'nearest_count', 'no', 'no_bump_scale', 'no_image',
        'no_reflection', 'no_shadow', 'noise_generator', 'normal',
        'normal_indices', 'normal_map', 'normal_vectors', 'number_of_waves',
        'object', 'octaves', 'off', 'offset', 'omega', 'omnimax', 'on', 'once',
        'onion', 'open', 'orient', 'orientation', 'orthographic',
        'panoramic', 'parallel', 'parametric', 'pass_through', 'pattern',
        'perspective', 'pgm', 'phase', 'phong', 'phong_size', 'photons',
        'pi', 'pigment', 'pigment_map', 'pigment_pattern', 'planar', 'plane',
        'png', 'point_at', 'poly', 'poly_wave', 'polygon', 'pot', 'pow', 'ppm',
        'precision', 'precompute', 'pretrace_end', 'pretrace_start', 'prism',
        'prod', 'projected_through', 'pwr',
        'quadratic_spline', 'quadric', 'quartic', 'quaternion', 'quick_color',
        'quick_colour', 'quilted',
        'radial', 'radians', 'radiosity', 'radius', 'rainbow', 'ramp_wave',
        'rand', 'range', 'ratio', 'read', 'reciprocal', 'recursion_limit',
        'red', 'reflection', 'reflection_exponent', 'refraction', 'render',
        'repeat', 'rgb', 'rgbf', 'rgbft', 'rgbt', 'right', 'ripples', 'rotate',
        'roughness',
        'samples', 'save_file', 'scale', 'scallop_wave', 'scattering', 'seed',
        'select', 'shadowless', 'sin', 'sine_wave', 'sinh', 'size', 'sky',
        'sky_sphere', 'slice', 'slope', 'slope_map', 'smooth', 'smooth_triangle',
        'solid', 'sor', 'spacing', 'specular', 'sphere', 'sphere_sweep',
        'spherical', 'spiral1', 'spiral2', 'spline', 'split_union', 'spotlight',
        'spotted', 'sqr', 'sqrt', 'statistics', 'str', 'strcmp', 'strength',
        'strlen', 'strlwr', 'strupr', 'sturm', 'substr', 'sum', 'superellipsoid',
        'switch', 'sys',
        't', 'tan', 'tanh', 'target', 'text', 'texture', 'texture_list',
        'texture_map', 'tga', 'thickness', 'threshold', 'tiff', 'tightness',
        'tile2', 'tiles', 'tolerance', 'toroidal', 'torus', 'trace', 'transform',
        'translate', 'transmit', 'triangle', 'triangle_wave', 'true', 'ttf',
        'turb_depth', 'turbulence', 'type',
        'u', 'u_steps', 'ultra_wide_angle', 'undef', 'union', 'up', 'use_alpha',
        'use_color', 'use_colour', 'use_index', 'utf8', 'uv_indices',
        'uv_mapping', 'uv_vectors',
        'v', 'v_steps', 'val', 'variance', 'vaxis_rotate', 'vcross', 'vdot',
        'version', 'vertex_vectors', 'vlength', 'vnormalize', 'vrotate', 'vstr',
        'vturbulence',
        'warning', 'warp', 'water_level', 'waves', 'while', 'width', 'wood',
        'wrinkles', 'write',
        'x', 'y', 'yes', 'z'
    ]

    _object_modifiers= [
        'ObjectModifier', 'Texture', 'Translate'
    ]

    def __init__(self, name, args=[], opts=[], kwargs=[]):
        """
            Base class for POV objects.

            @param name: POV object name
            @type name: string
            @param args: compulsory (comma separated?) pov args XX commas don't seem to matter?
            @type args: list
            @param opts: eg. CSG items
            @type opts: list
            @param kwargs: key value pairs
            @type kwargs: dict

            @TODO: move indentation check to own function
        """
        debug("%s: SceneItem.__init__(): Start: %s, %s, %s, %s" %
              (self.__class__.__name__, name, args, opts, kwargs))

        # format parameters
        self._format_args(args)
        self._format_opts(opts)
        self._format_kwargs(kwargs)

        # @todo: Does indentation really have to stay in the constructor??
        if not "indentation" in globals():
            global indentation
            indentation = 0
            debug("set initial indentation to 0")

        # Call syntax check methods
        self._check_arguments()
        self._check_opts()
        self._check_kwargs()

        self.name = name

        debug("%s: SceneItem.__init__(): Stop: %s, %s, %s, %s" %
              (self.__class__.__name__, name, args, opts, kwargs))

    #---------------------------------------------------------------------------
    # Pseudo private  methods
    #---------------------------------------------------------------------------

    def _indent(self):
        """
            Indent PoV code
        """
        global indentation
        indentation += 1
        debug("indent: %s", indentation)

    def _dedent(self):
        """
            Dedent PoV code
        """
        global indentation

        if not indentation > 0:
            raise IllegalStateException('Indentation below zero')

        indentation -= 1
        debug("dedent: %s", indentation)

    def _getIndent(self):
        """
            Get indentation
        """
        global indentation
        return indentation

    def _block_begin(self):
        """
            Begin code block
                * return opening bracket and line separator
                * increase indentation
        """
        debug("begin block")
        code = " {" + os.linesep

        self._indent()

        return code

    def _block_end(self):
        """
            End code block
                * reduce indentation
                * add line with closing bracket
        """
        debug("end block: indentation= %s", indentation)

        if indentation == 0:
            # blank line if this is a top level end
            code = self._getLine()
        else:
            self._dedent()
            code = self._getLine("}")

        return code

    def _getLine(self, s=""):
        """
            format line of code with indentation and line separator
        """
        global indentation
        info("'" + "  " * indentation + s + "'")
        return "  " * indentation + s + os.linesep

    def _check_opts(self):
        '''
            Option Syntax checks

            to be overwritten in subclasses
        '''
        pass

    def _check_arguments(self):
        '''
            Argument Syntax checks

            to be overwritten in subclasses
        '''
        pass

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks

            to be overwritten in subclasses
        '''
        pass

    def _validate_args(self, valid_args):
        '''
            Typecheck mandatory args agains given lost

            @TODO: make valid_args a fixed list of arguments?
        '''
        # args validation against objects list
        for i in range(len(self.args)):
            # type of  arguments
            if isinstance(valid_args[i], (list, tuple)):
                if not self.args[i].__class__.__name__ in valid_args[i]:
                    raise SdlSyntaxException('Value of Argument %s is expectet to be type %s but got %s' %
                                             (i, valid_args[i], self.args[i].__class__.__name__))
            else:
                if not self.args[i].__class__.__name__ == valid_args[i]:
                    raise SdlSyntaxException('Value of Argument %s is expectet to be type %s but got %s' %
                                             (i, valid_args[i], self.args[i].__class__.__name__))

    def _validate_opts(self, valid_opts):
        '''
            Typecheck Keywords agains givien dictionary
        '''
        # make sure only valid object modifiers are passed
        for i in range(len(self.opts)):
            if not self.opts[i].__class__.__name__ in valid_opts:
                raise SdlSyntaxException('Invalid option type %s not in allowed opts \n%s' %
                                         (self.opts[i].__class__.__name__, valid_opts))

    def _validate_kwargs(self, valid_kw):
        '''
            Typecheck Keywords agains givien dictionary
        '''
        # kwargs validation against objects dictionary
        for key, val in self.kwargs.items():
            # kwargs validation against global list
            if not self._is_valid_keyword(key):
                raise SdlSyntaxException('No such Keyword: ' + str(key))

            # allowed keywords
            if not key in valid_kw:
                raise SdlSyntaxException('Keyword %s not allowed for object %s' %
                                         (key, self.__class__.__name__))
            # type of kw arguments
            if not val.__class__.__name__ == valid_kw[key]:
                raise SdlSyntaxException('Value of KW Argument %s is expectet to be type %s but got %s' %
                                         (key, valid_kw[key], val.__class__.__name__))

    def _checkKwargValue(self, kwarg, validvalues):
        '''
            Check value range for kwargs
        '''
        if kwarg in self.kwargs:
            if not self.kwargs[kwarg] in validvalues:
                raise SdlSyntaxException(
                    'Value of KW Argument %s is expectet to be in %s but got %s: ' %
                    (kwarg, validvalues, self.kwargs[kwarg])
                )

    def _format_args(self, args):
        '''
            format argument parameters
        '''
        args = list(args)
        for i in range(len(args)):
            args[i] = self.map_arg(args[i])
        self.args = self.flatten(args)

    def _format_opts(self, opts):
        '''
            format option parameters
        '''
        opts = list(opts)
        for i in range(len(opts)):
            opts[i] = self.map_arg(opts[i])
        self.opts = self.flatten(opts)

    def _format_kwargs(self, kwargs):
        '''
            format keyword parameters
        '''
        #debug('kwargs: %s', kwargs)
        self.kwargs = dict(kwargs)  # take a copy
        kwargs = dict(kwargs).items()
        #debug('kwargs: %s', kwargs)
        kwargs.reverse()
        #debug('kwargs: %s', kwargs)

        for key, val in kwargs:
            if type(val) == tuple or type(val) == list:
                self.kwargs[key] = self.map_arg(val)

    def _is_valid_keyword(self, name):
        '''
            Test if keyword is Valid
        '''
        if name in self.__reserved_keywords:
            return True
        return False

    def _is_valid_identifier(self, name):
        '''
            Test if name is not a keyword
        '''
        if name not in self.__reserved_keywords:
            return True
        return False

    #---------------------------------------------------------------------------
    # Overloading magic methods
    #---------------------------------------------------------------------------

    def __str__(self):
        """
            return PoV code as string representation

            this method is meant to be overridden in subclasses
        """
        debug("%s: SceneItem.__str__(): %s, %s, %s" %
              (self.__class__.__name__, self.name, self.args, self.opts))

        return self.name

    def __setitem__(self, i, item):
        """
            Set Item magic method

            e.g. foo[i] = bar
        """
        if i < len(self.args):
            self.args[i] = self.map_arg(item)
        else:
            i -= len(self.args)
            if i < len(self.opts):
                self.opts[i] = self.map_arg(item)
            else:
                raise IndexError()

    def __getitem__(self, i):
        """
            Get Item magic method

            e.g. foo = bar[i]
        """
        if i < len(self.args):
            return self.args[i]
        else:
            i -= len(self.args)
            if i < len(self.opts):
                return self.opts[i]
            else:
                raise IndexError()

    def __eq__(self, other):
        '''
            Operator Overload "="
        '''
        if not isinstance(other, SceneItem):
            raise TypeError('can only be compared to objects of same type')
        a = self.name == other.name
        debug(str(self.name) + ' = ' + str(self.name))
        b = self.args == other.args
        debug(str(self.args) + ' = ' + str(self.args))
        c = self.opts == other.opts
        debug(str(self.opts) + ' = ' + str(self.opts))
        d = self.kwargs == other.kwargs
        debug(str(self.kwargs) + ' = ' + str(self.kwargs))
        return a & b & c & d

    #---------------------------------------------------------------------------
    # Public methods
    #---------------------------------------------------------------------------

    def append(self, *opts, **kwargs):
        """
            append Subitem(s) to Item

            works for Options and kwargs
        """

        for item in self.flatten(opts):
            self.opts.append(item)
        for key, val in kwargs.items():
            self.kwargs[key] = val

        # syntax check all options including appended stuff
        # need to check everything to get duplicate options etc.
        self._check_opts()
        self._check_kwargs()

    def map_arg(self, arg):
        """
            Map an argument list to an appropriate format
        """
        if type(arg) in (tuple, list):
            # if multiple-component, floating-point value, return a vector
            if len(arg) and hasattr(arg[0], "__float__"):
                return Vector(arg)
        # else return the same format as the input value
        return arg

    def flatten(self, seq):
        '''
            flatten lists to one dimension
        '''
        seq = list(seq)
        i = 0
        while i < len(seq):
            if type(seq[i]) in (list, tuple):
                x = seq.pop(i)
                for item in x:
                    seq.insert(i, item)
                    i += 1
            else:
                i += 1
        return seq
