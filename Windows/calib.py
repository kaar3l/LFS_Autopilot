from numpy import *
import numpy as np
from math import sqrt
import time
import math
#import ctypes
#import win32api
import socket
from simpleOSC import *
import random


initOSCClient('127.0.0.1', 55000)
a=1
b=0
c=-1
	# basic message
time.sleep(2)
sendOSCMsg( '/hor', [a] )
time.sleep(1)
sendOSCMsg( '/vert', [a] )
time.sleep(1)
sendOSCMsg( '/hor', [c] )
time.sleep(1)
sendOSCMsg( '/vert', [c] )
time.sleep(1)
sendOSCMsg( '/hor', [a] )
time.sleep(1)
sendOSCMsg( '/vert', [c] )
time.sleep(1)
sendOSCMsg( '/hor', [c] )
time.sleep(1)
sendOSCMsg( '/vert', [a] )
time.sleep(1)
sendOSCMsg( '/hor', [b] )
time.sleep(1)
sendOSCMsg( '/vert', [b] )
