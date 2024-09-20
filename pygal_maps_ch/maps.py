# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2015 Kozea, Serge Droz
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
Swiss cantons map

"""

from __future__ import division
from pygal.graph.map import BaseMap
import os


CANTONS = {
    'kt-zh': "ZH",
    'kt-be': "BE",
    'kt-lu': "LU",
    'kt-ju': "JH",
    'kt-ur': "UR",
    'kt-sz': "SZ",
    'kt-ow': "OW",
    'kt-nw': "NW",
    'kt-gl': "GL",
    'kt-zg': "ZG",
    'kt-fr': "FR",
    'kt-so': "SO",
    'kt-bl': "BL",
    'kt-bs': "BS",
    'kt-sh': "SH",
    'kt-ar': "AR",
    'kt-ai': "AI",
    'kt-sg': "SG",
    'kt-gr': "GR",
    'kt-ag': "AG",
    'kt-tg': "TG",
    'kt-ti': "TI",
    'kt-vd': "VD",
    'kt-vs': "VS",
    'kt-ne': "NE",
    'kt-ge': "GE",
}


with open(os.path.join(
        os.path.dirname(__file__),
        'ch.cantons.svg')) as file:
    CNT_MAP = file.read()


class Cantons(BaseMap):
    """Swiss Cantons map"""
    x_labels = list(CANTONS.keys())
    area_names = CANTONS
    area_prefix = 'z'
    kind = 'canton'
    svg_map = CNT_MAP
