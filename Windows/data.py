from numpy import *

data = loadtxt("xy.dat")
x,y,speed = data[:,0], data[:,1], data[:,2]
print speed
