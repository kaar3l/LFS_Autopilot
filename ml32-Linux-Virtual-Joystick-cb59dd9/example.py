import vjoy, math
import time
from numpy import *
import pyinsim

# This function returns essential joystick information
def getVJoyInfo():
	return {
		'name':       'Logtech G94', # The name of the virtual joystick
		'relaxis':    [], # List of relative axises to use
		'absaxis':    [vjoy.ABS_X, vjoy.ABS_Y], # List of absolute axises to use
		'feedback':   [], # List of force feedback types to support
		'maxeffects': 4, # Maximum number of concurrent feedback effects 
		'buttons':    []  # List of buttons to use
	}

# The "think" routine runs every few milliseconds.  Do NOT perform
# blocking operations within this function.  Doing so will prevent other
# important stuff from happening.
theta = 0.0
def doVJoyThink():
    global theta
    theta += 0.05
    events = []
    x      = int(math.cos(theta) * 32500)
    y      = int(math.sin(theta) * 32500)
    insim.send(pyinsim.ISP_MST, Msg='tore')
    events.append([vjoy.EV_ABS, vjoy.ABS_X, x])
    events.append([vjoy.EV_ABS, vjoy.ABS_Y, y])
    print theta
    insim.send(pyinsim.ISP_MST, Msg='Hello, InSim!')
    pyinsim.run()
    print "2"
    return events

insim = pyinsim.insim('127.0.0.1', 29999, Admin='password')
#pyinsim.run()
