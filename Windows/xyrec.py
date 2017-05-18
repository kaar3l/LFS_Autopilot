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
import pickle

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
                print info.X, info.Y, info.Z, info.Speed/100, info.Heading/180, info.PLID, npl.PName
#                savetxt("xy.dat", info.X, info.Y, info.Speed/100, info.Heading/180, info.PLID, npl.PName)
#                savetxt('myfile.txt', info.X, info.Y, info.Speed/100, info.Heading/180, info.PLID, npl.PName, fmt="%12.6G")
# Initialize InSim.
insim = pyinsim.insim('127.0.0.1', 29999, Flags=pyinsim.ISF_MCI, 
                      Interval=500, Admin='')

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
