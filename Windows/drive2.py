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
def punkti_nr(xarray,xvalue,yarray,yvalue,zarray,zvalue):
    l2him=(np.abs((xarray-xvalue)**2+(yarray-yvalue)**2)+(zarray-zvalue)**2).argmin()
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
    print " "
    print " "
    print "ALGUS"
    n=0
    players_x=[]
    players_y=[]
    players_z=[]
    players_speed=[]
    players_heading=[]
    players_plid=[]
    players_pname=[]
    for info in mci.Info:
        # Try get the player for this car (sometimes get MCI 
        # packet before all players have been received).
        npl = players.get(info.PLID)

        if npl:
            # Print the player's name.
        	#print npl.PName, info.PLID
		#print info.X, info.Y, info.Speed/100, info.Heading/180, info.PLID, npl.PName
	        players_x.insert(n,info.X)
	        players_y.insert(n,info.Y)
		players_z.insert(n,info.Z)
	        players_speed.insert(n,info.Speed/100)
	        players_heading.insert(n,info.Heading/180)
		players_plid.insert(n,info.PLID)
		players_pname.insert(n,npl.PName)		
#		print n
		n=n+1
#    print players_x
#    print players_y
#   print players_z
#    print players_speed
#    print players_heading
#    print players_plid
#    print players_pname
#M2ngija nimi
    name="Kaarel"
    for item in players_pname:
        if item in name:
	    player_number=players_pname.index(name)
	    print "Enda andmed"
            print player_number, players_plid[player_number], "X:", players_x[player_number], "Y:", players_y[player_number], players_speed[player_number],players_heading[player_number], players_pname[player_number]
	    X=players_x[player_number]
	    Y=players_y[player_number]
	    Z=players_z[player_number]
	    Speed=players_speed[player_number]
	    Heading=players_heading[player_number]

#Import data
	    data = genfromtxt("xy.dat")
	    X_rada,Y_rada,Z_rada,V_rada,H_rada,P_number= data[:,0], data[:,1], data[:,2], data[:,3], data[:,4], data[:,5]
#Leiame l2hima punkti numbri

	    P_number=(punkti_nr(X_rada,X,Y_rada,Y,Z_rada,Z))
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
	    MAX_STEERNG_ANGLE=60 #LFSi steering angle*2 XFG=60
	    turnaxis=angdiff
	    if angdiff>MAX_STEERNG_ANGLE:
		turnaxis=1
	    elif angdiff<-MAX_STEERNG_ANGLE:
		turnaxis=-1
	    else:
		turnaxis=(angdiff+MAX_STEERNG_ANGLE)/MAX_STEERNG_ANGLE-1
#Kiiruse seadmine spd_div saab olla -1 .... 1
            Speed2=Speed
#Lubatud kiiruse viga -1....+1
            max_speed=P_speed+1
            min_speed=P_speed-1
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

	#Punkt auto ees
 #           r=6.1*65536 #1.punkti kaugus
 #           r2=12*65536 #1.punkti kaugus
 #           r3=18*65536 #1.punkti kaugus
 #           ohutu_kaugus=(65536*6)**2 #raadius punkti ymber

#	    usr_dir=Heading/180+90
#		r=6.1*65536
#1. Punkt auto ees
#	    delta_x=r*cos(math.radians(usr_dir))+X
#	    delta_y=r*sin(math.radians(usr_dir))+Y
#2. Punkt auto ees
#	    delta_x2=r2*cos(math.radians(usr_dir))+usr_x
#	    delta_y2=r2*sin(math.radians(usr_dir))+usr_y
#3. Punkt auto ees
#	    delta_x3=r3*cos(math.radians(usr_dir))+usr_x
#	    delta_y3=r3*sin(math.radians(usr_dir))+usr_y	    
#	    print ohutu_kaugus
#            m=0
    #Pidurdamine kui keegi on tee peal ees
#	    for item in players_pname:
 #           	player_to_other=(delta_x-players_x[m])**2+(delta_y-players_y[m])**2
#            	player_to_other2=sqrt((delta_x2-players_x[m])**2+(delta_y2-players_y[m])**2)
#            	player_to_other3=sqrt((delta_x3-players_x[m])**2+(delta_y3-players_y[m])**2)
#		print player_to_other
#		m=m+1
#Kui auto satub punkti lahedale siis:
#		print player_to_other
#		if player_to_other<ohutu_kaugus:
#			print ">>>BRAKE<<< 6,1m"
#			speedaxis=-1
#		elif player_to_other2<ohutu_kaugus:
#			print ">>>BRAKE<<< 12m"
#			speedaxis=-0.9
#		elif player_to_other3<ohutu_kaugus:
#			print ">>>BRAKE<<< 18m"
#			speedaxis=-0.9
	    r=6.1*65536
	    r2=12*65536
	    r3=18*65536
	    ohutu_kaugus=(4*65536)**2
	    ohutu_kaugus2=(5*65536)**2
	    ohutu_kaugus3=(6*65536)**2
	    print "ohutu", ohutu_kaugus, Heading
#	    usr_dir=Heading/180+90
	    usr_dir=Heading+90
	    print Heading
	    print usr_dir
	    m=0
		#Punkt auto ees
	    delta_x=r*cos(math.radians(usr_dir))+X
	    delta_y=r*sin(math.radians(usr_dir))+Y
		#Teine punkt
	    delta_x2=r2*cos(math.radians(usr_dir))+X
	    delta_y2=r2*sin(math.radians(usr_dir))+Y
		#kolmas punkt
	    delta_x3=r3*cos(math.radians(usr_dir))+X
	    delta_y3=r3*sin(math.radians(usr_dir))+Y
		
	    for item in players_pname:
	        player_to_other=(delta_x-players_x[m])**2+(delta_y-players_y[m])**2
	        player_to_other2=(delta_x2-players_x[m])**2+(delta_y2-players_y[m])**2
	        player_to_other3=(delta_x3-players_x[m])**2+(delta_y3-players_y[m])**2
			
	        print "Vahemaa:", sqrt(((delta_x-players_x[m])/65536)**2+((delta_y-players_y[m])/65536)**2)
	        m=m+1
#	        print player_to_other
#Esimene punkt
	        if player_to_other<ohutu_kaugus:
#	           print player_to_other,ohutu_kaugus
	           print ">>>BRAKE<<< 6m"
	           speedaxis=-1
#Teine punkt
	        elif player_to_other2<ohutu_kaugus2:
#	           print player_to_other,ohutu_kaugus
	           print ">>>BRAKE<<< 12m"
	           speedaxis=-0.95
#Kolmas punkt
	        elif player_to_other3<ohutu_kaugus3:
#	           print player_to_other,ohutu_kaugus
	           print ">>>BRAKE<<< 18m"
	           speedaxis=-0.90
			   
#Axiste v2ljutamine
	    print "Horisontaal axise vaartus:", turnaxis
	    print "Vertikaal axise vaartus:", speedaxis
#turnaxise ja speedaxise export
	    initOSCClient('127.0.0.1', 55000)
	    sendOSCMsg( '/hor', [-turnaxis] )
	    sendOSCMsg( '/vert', [speedaxis] )


    print "LOPP"


# Initialize InSim.
insim = pyinsim.insim('127.0.0.1', 29999, Flags=pyinsim.ISF_MCI, 
                      Interval=20, Admin='')

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
