#!/usr/bin/env python
#
# helper.py - core library module for pyinsim
#
# Copyright 2008-2012 Alex McBride <xandermcbride@gmail.com>
#
# This software may be used and distributed according to the terms of the
# GNU Lesser General Public License version 2 or any later version.
#

import re
import math

__all__ = ['degrees_radians', 'distance', 'intersects', 'length_km', 'length_metres', 'length_miles', 'metres_km', 'metres_miles', 'mps_kph', 'mps_mph', 'radians_degress', 'radians_rpm', 'speed_kph', 'speed_mph', 'speed_mps', 'strip_colours', 'time', 'timestr']

# Constants.
COLOUR_REGEX = re.compile('\^[0-9]')

# Functions.
def strip_colours(s):
    """Strip colour codes (^7, ^3 etc..) from a string."""
    return COLOUR_REGEX.sub('', s) 

def time(ms):
    """Convert milliseconds to hours, minutes, seconds, thousandths."""
    return [int(ms / 3600000), 
            int(ms / 60000 % 60), 
            int(ms / 1000 % 60), 
            int(ms % 1000)]

def timestr(ms, hours=False):
    """Convert milliseconds to a formatted time str"""
    h, m, s, t = time(ms)
    if h or hours:
        return '{0}:{1:0>2}:{2:0>2}.{3:0>3}'.format(h, m, s, t)
    return '{0}:{1:0>2}.{2:0>3}'.format(m, s, t)

def speed_mps(speed):
    """Convert speed to metres per second."""
    return speed / 327.68

def speed_mph(speed):
    """Convert speed to miles per hour."""
    return speed / 146.486067

def speed_kph(speed):
    """Convert speed to kilometres per hour."""
    return speed / 91.02

def mps_mph(mps):
    """Convert metres per second to miles per hour."""
    return mps * 2.23

def mps_kph(mps):
    """Convert metres per second to kilometres per hour."""
    return mps * 3.6

def length_metres(length):
    """Convert length to metres."""
    return length / 65536.0

def length_miles(length):
    """Convert length to miles."""
    return length(length) / 1609.344

def length_km(length):
    """Convert length to kilometres."""
    return length(length) / 1000.0

def metres_miles(metres):
    """Convert metres to miles."""
    return metres / 1609.344

def metres_km(metres):
    """Convert metres to kilometres."""
    return metres / 1000.0

def radians_degress(radians):
    """Convert radians to degrees."""
    return radians * 57.295773

def degrees_radians(degrees):
    """Convert degrees to radians."""
    return degrees * 0.017453

def radians_rpm(radians):
    """Convert radians to RPM."""
    return radians * 9.549295;

def distance(a=(0,0,0), b=(0,0,0)):
    """Determin the distance between two points."""
    return math.sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]) + (b[2] - a[2]) * (b[2] - a[2]))

def intersects(rect1=(0, 0, 0, 0), rect2=(0, 0, 0, 0)):
    """Determin if two rectangles intersect (top, left, width, height)."""
    x1 = rect1[0] + rect1[2]
    y1 = rect1[1] + rect1[3]
    x3 = rect2[0] + rect2[2]
    y3 = rect2[1] + rect2[3]
    return not (x1 < rect2[0] or x3 < rect1[0] or y1 < rect2[1] or y3 < rect1[1])

if __name__ == '__main__':
    pass


