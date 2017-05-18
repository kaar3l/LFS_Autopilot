#import pyinsim
#
#def multi_car_info(insim, mci):
#    for info in mci.Info:
#        print '%d %d %d %d' % (info.X, info.Y, info.Speed/100, info.Heading/180)
#
#insim = pyinsim.insim('127.0.0.1', 29999, Flags=pyinsim.ISF_MCI, Interval=500, Admin='password')
#
#insim.bind(pyinsim.ISP_MCI, multi_car_info)
#
#pyinsim.run()
import pyinsim
from numpy import *
import numpy as np
from math import sqrt
import time
import math
import socket
from simpleOSC import *
import random

# Store connections and players in dictionaries with their 
# UCIDs and PLIDs as the keys.
connections = {}
players = {}

# Called whenever a host is joined.
def insim_multi(insim, ism):
    # Request all connection packets are sent.
    insim.send(pyinsim.ISP_TINY, ReqI=1, SubT=pyinsim.TINY_NCN)
    # Request all player packets are sent.
    insim.send(pyinsim.ISP_TINY, ReqI=1, SubT=pyinsim.TINY_NPL)



# Called when a connection joins the host.
def new_connection(insim, ncn):
    # Add to connections dict.
    connections[ncn.UCID] = ncn



# Called when a connection leaves the host.
def connection_leave(insim, cnl):
    # Delete connection from dict.
    del connections[cnl.UCID]


    
# Called when a player joins the race
def new_player(insim, npl):
    # Add to players dict.
    players[npl.PLID] = npl
    
# Called when a player leaves the race (spectate etc..)
def player_leave(insim, pll):
    # Delete from players dict.
    del players[pll.PLID]


#L2hima punkti nr
def punkti_nr(xarray,xvalue,yarray,yvalue):
    l2him=(np.abs((xarray-xvalue)**2+(yarray-yvalue)**2)).argmin()
    return l2him
#Punkti nr -> kiirus
def P_vastav(punktinr,vektor):
    speed=punktinr
    return vektor[speed]
#L2hima punkti kaugus
def kaugus(xarray,xvalue,yarray,yvalue):
    l2him=(np.abs((xarray-xvalue)**2+(yarray-yvalue)**2)).argmin()
    return sqrt(abs((xarray[l2him]-xvalue)**2+(yarray[l2him]-yvalue)**2))


    
# Called once every second with car info.
def multi_car_info(insim, mci):
    # Loop through each car in the packet.
    for info in mci.Info:
        # Try get the player for this car (sometimes get MCI 
        # packet before all players have been received).
        npl = players.get(info.PLID)
        if npl:
            # Print the player's name.
#            print npl.PName
            if npl.PName=="Kaarel":
                print " "
                print " "
                print "Praegused koordinaadid:"
		print info.X, info.Y, info.Speed/100, info.Heading/180, info.PLID, npl.PName
#X Y Speed Heading on siis soitva auto andmed	
		X=info.X
		Y=info.Y
		Speed=info.Speed/100
		Heading=info.Heading/180
#Impordime data failist
#		data = loadtxt("xy.dat")
		data = genfromtxt("xy.dat")
		X_rada,Y_rada,V_rada,H_rada,P_number= data[:,0], data[:,1], data[:,2], data[:,3], data[:,4]
#Leiame l2hima punkti numbri

		P_number=(punkti_nr(X_rada,info.X,Y_rada,info.Y))
		P_speed=(P_vastav(P_number,V_rada))
		print "L2hima punkti number:",P_number,"Kiirus punktis:",P_speed
#J2rgmine punkti
		next_point=P_number+1
#Uue punkti koordinaadid
		next_x=(P_vastav(next_point,X_rada))
		next_y=(P_vastav(next_point,Y_rada))
#Uue ja enda punkti vahe
		diff_x=next_x-X
		diff_y=next_y-Y
		print "J2rgmise punkti X:", next_x
		print "J2rgmise punkti Y:", next_y

#Uue ja enda vaheline kaugus suht ebavajalik
#		diff_dst=sqrt(diff_x**2+diff_y**2)

		print "Punkti ja auto vahe diff x:", diff_x ,"diff_y:",diff_y

#6ige suund -1 ja 1 vahel

		diff_alfa=-math.atan2(diff_x,diff_y)*180/math.pi+360

		angdiff=((diff_alfa-Heading+180+360)%360)-180
		print "Angular difference",angdiff
#Keeramine
		turnaxis=angdiff
		if angdiff>45:
			turnaxis=1
		elif angdiff<-45:
			turnaxis=-1
		else:
			turnaxis=(angdiff+45)/45-1
#Kiiruse seadmine spd_div saab olla -1 .... 1
        	Speed2=Speed
#Lubatud kiiruse viga -1....+1
        	max_speed=P_speed+2
        	min_speed=P_speed-2
#Kiirus/punkti kiirus ehk siis 0....1
		spd_div=Speed2/P_speed
#0-ga jagamine
       		if P_speed==0:
            		spd_div=1
#J22b -2 ja 2 piiri:
        	elif Speed2<max_speed:
            		spd_div=0
        	elif Speed2>min_speed:
            		spd_div=0
#Kiirus j22b piiridest v2lja
        	if Speed2>max_speed:
            #Korrutatav muudab seda lineearset ala pikkust
            		spd_div=-(Speed2/P_speed-1)*4
            #Kiirus j22b juba yle 10kmh suuremaks
            		if spd_div<-1:
                		spd_div=-1
        	if Speed2<min_speed:
            #Korrutatav muudab seda lineearset ala pikkust
            		spd_div=-(Speed2/P_speed-1)*4
            	if spd_div>1:
                	spd_div=1
            #gaasi andmise kahandamine kui auto nurk pole oige
		print "spd_div=",spd_div
		if spd_div>0:
		#ainult kui antakse gaasi voetakse nurka arvesse
			print "Gaasi maha"
			speedaxis=spd_div-abs(turnaxis)*0.5 #0.5 suurendades saab vale nurga all oleva auto gaasi vahendada
                else:
                        speedaxis=spd_div
		print "Horisontaal axise vaartus:", turnaxis
		print "Vertikaal axise vaartus:", speedaxis

#Saatmine joysticki programmi:
#Tuleb windowsile kommentaar maha votta
		initOSCClient('127.0.0.1', 55000)

		# basic message
		sendOSCMsg( '/hor', [-turnaxis] )
		sendOSCMsg( '/vert', [speedaxis] )







#Peaprogre lopp
# Initialize InSim.
insim = pyinsim.insim('127.0.0.1', 29999, Flags=pyinsim.ISF_MCI, 
                      Interval=50, Admin='')

# Bind packet events.
insim.bind(pyinsim.ISP_ISM, insim_multi)
insim.bind(pyinsim.ISP_NCN, new_connection)
insim.bind(pyinsim.ISP_CNL, connection_leave)
insim.bind(pyinsim.ISP_NPL, new_player)
insim.bind(pyinsim.ISP_PLL, player_leave)
insim.bind(pyinsim.ISP_MCI, multi_car_info)

# When first connected request current host info.
insim.send(pyinsim.ISP_TINY, ReqI=1, SubT=pyinsim.TINY_ISM)

# Run packet receive loop.
pyinsim.run()
