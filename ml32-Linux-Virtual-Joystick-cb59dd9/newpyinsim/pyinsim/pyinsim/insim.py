#!/usr/bin/env python
#
# insim.py - core library module for pyinsim
#
# Copyright 2008-2012 Alex McBride <xandermcbride@gmail.com>
#
# This software may be used and distributed according to the terms of the
# GNU Lesser General Public License version 2 or any later version.
#

import struct
from pyinsim.lfstr import str_factory

__all__ = ['BFN_CLEAR', 'BFN_DEL_BTN', 'BFN_REQUEST', 'BFN_USER_CLEAR', 'CAR_ALL', 'CAR_BF1', 'CAR_FBM', 'CAR_FO8', 'CAR_FOX', 'CAR_FXO', 'CAR_FXR', 'CAR_FZ5', 'CAR_FZR', 'CAR_LX4', 'CAR_LX6', 'CAR_MRT', 'CAR_NONE', 'CAR_RAC', 'CAR_RB4', 'CAR_UF1', 'CAR_UFR', 'CAR_XFG', 'CAR_XFR', 'CAR_XRG', 'CAR_XRR', 'CAR_XRT', 'CCI_BLUE', 'CCI_FIRST', 'CCI_LAG', 'CCI_LAST', 'CCI_NONE', 'CCI_YELLOW', 'CONF_CONFIRMED', 'CONF_DID_NOT_PIT', 'CONF_DISQ', 'CONF_MENTIONED', 'CONF_NONE', 'CONF_PENALTY_30', 'CONF_PENALTY_45', 'CONF_PENALTY_DT', 'CONF_PENALTY_SG', 'CONF_TIME', 'CarContOBJ', 'CarContact', 'CompCar', 'DL_ABS', 'DL_BATTERY', 'DL_FULLBEAM', 'DL_HANDBRAKE', 'DL_NONE', 'DL_OILWARN', 'DL_PITSPEED', 'DL_SHIFT', 'DL_SIGNAL_ANY', 'DL_SIGNAL_L', 'DL_SIGNAL_R', 'DL_SPARE', 'DL_TC', 'HInfo', 'HOSTF_CAN_RESET', 'HOSTF_CAN_SELECT', 'HOSTF_CAN_VOTE', 'HOSTF_CRUISE', 'HOSTF_FCV', 'HOSTF_MID_RACE', 'HOSTF_MUST_PIT', 'HOSTF_NONE', 'HOS_FIRST', 'HOS_LAST', 'HOS_LICENSED', 'HOS_NONE', 'HOS_S1', 'HOS_S2', 'HOS_SPECPASS', 'INSIM_VERSION', 'INST_ALWAYS_ON', 'IRP_ARP', 'IRP_ARQ', 'IRP_ERR', 'IRP_HLR', 'IRP_HOS', 'IRP_SEL', 'IR_ARP', 'IR_ARQ', 'IR_ERR', 'IR_ERR_ADMIN', 'IR_ERR_HOSTNAME', 'IR_ERR_NONE', 'IR_ERR_NOSPEC', 'IR_ERR_PACKET', 'IR_ERR_PACKET2', 'IR_ERR_SPEC', 'IR_HLR', 'IR_HOS', 'IR_SEL', 'ISB_CANCEL', 'ISB_CLICK', 'ISB_CTRL', 'ISB_DARK', 'ISB_LEFT', 'ISB_LIGHT', 'ISB_LIGHT_GREY', 'ISB_LMB', 'ISB_NONE', 'ISB_OK', 'ISB_RIGHT', 'ISB_RMB', 'ISB_SELECTED_TEXT', 'ISB_SHIFT', 'ISB_TEXT_STRING', 'ISB_TITLE_COLOUR', 'ISB_UNAVAILABLE', 'ISB_UNSELECTED_TEXT', 'ISF_AXM_EDIT', 'ISF_AXM_LOAD', 'ISF_CON', 'ISF_HLV', 'ISF_LOCAL', 'ISF_MCI', 'ISF_MSO_COLS', 'ISF_NLP', 'ISF_NONE', 'ISF_OBH', 'ISF_RES_0', 'ISF_RES_1', 'ISP_ACR', 'ISP_AXI', 'ISP_AXM', 'ISP_AXO', 'ISP_BFN', 'ISP_BTC', 'ISP_BTN', 'ISP_BTT', 'ISP_CCH', 'ISP_CNL', 'ISP_CON', 'ISP_CPP', 'ISP_CPR', 'ISP_CRS', 'ISP_FIN', 'ISP_FLG', 'ISP_HLV', 'ISP_III', 'ISP_ISI', 'ISP_ISM', 'ISP_LAP', 'ISP_MCI', 'ISP_MOD', 'ISP_MSL', 'ISP_MSO', 'ISP_MST', 'ISP_MSX', 'ISP_MTC', 'ISP_NCN', 'ISP_NLP', 'ISP_NONE', 'ISP_NPL', 'ISP_OBH', 'ISP_PEN', 'ISP_PFL', 'ISP_PIT', 'ISP_PLA', 'ISP_PLC', 'ISP_PLL', 'ISP_PLP', 'ISP_PSF', 'ISP_REO', 'ISP_RES', 'ISP_RIP', 'ISP_RST', 'ISP_SCC', 'ISP_SCH', 'ISP_SFP', 'ISP_SMALL', 'ISP_SPX', 'ISP_SSH', 'ISP_STA', 'ISP_TINY', 'ISP_TOC', 'ISP_VER', 'ISP_VTN', 'ISS_16', 'ISS_FRONT_END', 'ISS_GAME', 'ISS_MPSPEEDUP', 'ISS_MULTI', 'ISS_NONE', 'ISS_PAUSED', 'ISS_REPLAY', 'ISS_SHIFTU', 'ISS_SHIFTU_FOLLOW', 'ISS_SHIFTU_NO_OPT', 'ISS_SHOW_2D', 'ISS_SOUND_MUTE', 'ISS_VIEW_OVERRIDE', 'ISS_VISIBLE', 'ISS_WINDOWED', 'IS_ACR', 'IS_AXI', 'IS_AXM', 'IS_AXO', 'IS_BFN', 'IS_BTC', 'IS_BTN', 'IS_BTT', 'IS_CCH', 'IS_CNL', 'IS_CON', 'IS_CPP', 'IS_CPR', 'IS_CRS', 'IS_FIN', 'IS_FLG', 'IS_HLV', 'IS_III', 'IS_ISI', 'IS_ISM', 'IS_LAP', 'IS_MCI', 'IS_MOD', 'IS_MSL', 'IS_MSO', 'IS_MST', 'IS_MSX', 'IS_MTC', 'IS_NCN', 'IS_NLP', 'IS_NPL', 'IS_OBH', 'IS_PEN', 'IS_PFL', 'IS_PIT', 'IS_PLA', 'IS_PLC', 'IS_PLL', 'IS_PLP', 'IS_PSF', 'IS_REO', 'IS_RES', 'IS_RIP', 'IS_RST', 'IS_SCC', 'IS_SCH', 'IS_SFP', 'IS_SMALL', 'IS_SPX', 'IS_SSH', 'IS_STA', 'IS_TINY', 'IS_TOC', 'IS_VER', 'IS_VTN', 'IS_X_MAX', 'IS_X_MIN', 'IS_Y_MAX', 'IS_Y_MIN', 'LEAVR_BANNED', 'LEAVR_DISCO', 'LEAVR_KICKED', 'LEAVR_LOSTCONN', 'LEAVR_SECURITY', 'LEAVR_TIMEOUT', 'MSO_O', 'MSO_PREFIX', 'MSO_SYSTEM', 'MSO_USER', 'NodeLap', 'OBH_CAN_MOVE', 'OBH_LAYOUT', 'OBH_NONE', 'OBH_ON_SPOT', 'OBH_WAS_MOVING', 'OG_BAR', 'OG_CTRL', 'OG_KM', 'OG_NONE', 'OG_SHIFT', 'OG_TURBO', 'ObjectInfo', 'OutGaugePack', 'OutSimPack', 'PENALTY_30', 'PENALTY_45', 'PENALTY_DT', 'PENALTY_DT_VALID', 'PENALTY_NONE', 'PENALTY_SG', 'PENALTY_SG_VALID', 'PENR_ADMIN', 'PENR_FALSE_START', 'PENR_SPEEDING', 'PENR_STOP_LATE', 'PENR_STOP_SHORT', 'PENR_UNKNOWN', 'PENR_WRONG_WAY', 'PIF_AUTOCLUTCH', 'PIF_AUTOGEARS', 'PIF_AXIS_CLUTCH', 'PIF_CUSTOM_VIEW', 'PIF_HELP_B', 'PIF_INPITS', 'PIF_KB_NO_HELP', 'PIF_KB_STABILISED', 'PIF_MOUSE', 'PIF_NONE', 'PIF_RESERVED_2', 'PIF_RESERVED_32', 'PIF_RESERVED_4', 'PIF_SHIFTER', 'PIF_SWAPSIDE', 'PITLANE_DT', 'PITLANE_ENTER', 'PITLANE_EXIT', 'PITLANE_NO_PURPOSE', 'PITLANE_SG', 'PMO_ADD_OBJECTS', 'PMO_CLEAR_ALL', 'PMO_DEL_OBJECTS', 'PMO_LOADING_FILE', 'PSE_BODY_MAJOR', 'PSE_BODY_MINOR', 'PSE_FR_DAM', 'PSE_FR_WHL', 'PSE_LE_FR_DAM', 'PSE_LE_FR_WHL', 'PSE_LE_RE_DAM', 'PSE_LE_RE_WHL', 'PSE_NONE', 'PSE_NOTHING', 'PSE_REFUEL', 'PSE_RE_DAM', 'PSE_RE_WHL', 'PSE_RI_FR_DAM', 'PSE_RI_FR_WHL', 'PSE_RI_RE_DAM', 'PSE_RI_RE_WHL', 'PSE_SETUP', 'PSE_STOP', 'RIPOPT_FULL_PHYS', 'RIPOPT_LOOP', 'RIPOPT_NONE', 'RIPOPT_SKINS', 'RIP_ALREADY', 'RIP_CORRUPTED', 'RIP_DEDICATED', 'RIP_DEST_OOB', 'RIP_NOT_FOUND', 'RIP_NOT_REPLAY', 'RIP_OK', 'RIP_OOS', 'RIP_UNKNOWN', 'RIP_UNLOADABLE', 'RIP_USER', 'RIP_WRONG_MODE', 'SETF_ABS_ENABLE', 'SETF_NONE', 'SETF_SYMM_WHEELS', 'SETF_TC_ENABLE', 'SMALL_NLI', 'SMALL_NONE', 'SMALL_RTP', 'SMALL_SSG', 'SMALL_SSP', 'SMALL_STP', 'SMALL_TMS', 'SMALL_VTA', 'SND_ERROR', 'SND_INVALIDKEY', 'SND_MESSAGE', 'SND_SILENT', 'SND_SYSMESSAGE', 'SSH_CORRUPTED', 'SSH_DEDICATED', 'SSH_NO_SAVE', 'SSH_OK', 'TINY_AXC', 'TINY_AXI', 'TINY_CLOSE', 'TINY_CLR', 'TINY_GTH', 'TINY_ISM', 'TINY_MCI', 'TINY_MPE', 'TINY_NCN', 'TINY_NLP', 'TINY_NONE', 'TINY_NPL', 'TINY_PING', 'TINY_REN', 'TINY_REO', 'TINY_REPLY', 'TINY_RES', 'TINY_RIP', 'TINY_RST', 'TINY_SCP', 'TINY_SST', 'TINY_VER', 'TINY_VTC', 'TYRE_HYBRID', 'TYRE_KNOBBLY', 'TYRE_NOT_CHANGED', 'TYRE_R1', 'TYRE_R2', 'TYRE_R3', 'TYRE_R4', 'TYRE_ROAD_NORMAL', 'TYRE_ROAD_SUPER', 'VIEW_ANOTHER', 'VIEW_CAM', 'VIEW_CUSTOM', 'VIEW_DRIVER', 'VIEW_FOLLOW', 'VIEW_HELI', 'VOTE_END', 'VOTE_NONE', 'VOTE_QUALIFY', 'VOTE_RESTART', 'str_factory']

# Constants.
INSIM_VERSION = 5

# Packet Type.
ISP_NONE = 0
ISP_ISI = 1
ISP_VER = 2
ISP_TINY = 3
ISP_SMALL = 4
ISP_STA = 5
ISP_SCH = 6
ISP_SFP = 7
ISP_SCC = 8
ISP_CPP = 9
ISP_ISM = 10
ISP_MSO = 11
ISP_III = 12
ISP_MST = 13
ISP_MTC = 14
ISP_MOD = 15
ISP_VTN = 16
ISP_RST = 17
ISP_NCN = 18
ISP_CNL = 19
ISP_CPR = 20
ISP_NPL = 21
ISP_PLP = 22
ISP_PLL = 23
ISP_LAP = 24
ISP_SPX = 25
ISP_PIT = 26
ISP_PSF = 27
ISP_PLA = 28
ISP_CCH = 29
ISP_PEN = 30
ISP_TOC = 31
ISP_FLG = 32
ISP_PFL = 33
ISP_FIN = 34
ISP_RES = 35
ISP_REO = 36
ISP_NLP = 37
ISP_MCI = 38
ISP_MSX = 39
ISP_MSL = 40
ISP_CRS = 41
ISP_BFN = 42
ISP_AXI = 43
ISP_AXO = 44
ISP_BTN = 45
ISP_BTC = 46
ISP_BTT = 47
ISP_RIP = 48
ISP_SSH = 49
ISP_CON = 50
ISP_OBH = 51
ISP_HLV = 52
ISP_PLC = 53
ISP_AXM = 54
ISP_ACR = 55

# ISI Flags.
ISF_NONE = 0
ISF_RES_0 = 1
ISF_RES_1 = 2
ISF_LOCAL = 4
ISF_MSO_COLS = 8
ISF_NLP = 16
ISF_MCI = 32
ISF_CON = 64
ISF_OBH = 128
ISF_HLV = 256
ISF_AXM_LOAD = 512
ISF_AXM_EDIT = 1024

class IS_ISI:
    """InSim Init - packet to initialise the InSim system"""
    s = struct.Struct('3Bx2HxcH15sx15sx')
    def __init__(self, ReqI=0, UDPPort=0, Flags=ISF_NONE, Prefix='\x00', Interval=0, Admin='', IName=''):
        self.Size = 44
        self.Type = ISP_ISI
        self.ReqI = ReqI
        self.UDPPort = UDPPort
        self.Flags = Flags
        self.Prefix = Prefix
        self.Interval = Interval
        self.Admin = Admin
        self.IName = IName
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UDPPort, self.Flags, str_factory.encode(self.Prefix), self.Interval, str_factory.encode(self.Admin), str_factory.encode(self.IName))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UDPPort, self.Flags, self.Prefix, self.Interval, self.Admin, self.IName = self.s.unpack(data)
        self.Admin = str_factory.decode(self.Admin)
        self.IName = str_factory.decode(self.IName)
        return self

# TINY SubT
TINY_NONE = 0
TINY_VER = 1
TINY_CLOSE = 2
TINY_PING = 3
TINY_REPLY = 4
TINY_VTC = 5
TINY_SCP = 6
TINY_SST = 7
TINY_GTH = 8
TINY_MPE = 9
TINY_ISM = 10
TINY_REN = 11
TINY_CLR = 12
TINY_NCN = 13
TINY_NPL = 14
TINY_RES = 15
TINY_NLP = 16
TINY_MCI = 17
TINY_REO = 18
TINY_RST = 19
TINY_AXI = 20
TINY_AXC = 21
TINY_RIP = 22

class IS_TINY:
    """General purpose 4 byte packet"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, SubT=TINY_NONE):
        self.Size = 4
        self.Type = ISP_TINY
        self.ReqI = ReqI
        self.SubT = SubT
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.SubT)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.SubT = self.s.unpack(data)
        return self

# SMALL SubT
SMALL_NONE = 0
SMALL_SSP = 1
SMALL_SSG = 2
SMALL_VTA = 3
SMALL_TMS = 4
SMALL_STP = 5
SMALL_RTP = 6
SMALL_NLI = 7

class IS_SMALL:
    """General purpose 8 byte packet"""
    s = struct.Struct('4BI')
    def __init__(self, ReqI=0, SubT=SMALL_NONE, UVal=0):
        self.Size = 8
        self.Type = ISP_SMALL
        self.ReqI = ReqI
        self.SubT = SubT
        self.UVal = UVal
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.SubT, self.UVal)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.SubT, self.UVal = self.s.unpack(data)
        return self

class IS_VER:
    """VERsion"""
    s = struct.Struct('3Bx7sx5sxH')
    def __init__(self, ReqI=0, Version='', Product='', InSimVer=0):
        self.Size = 20
        self.Type = ISP_VER
        self.ReqI = ReqI
        self.Version = Version
        self.Product = Product
        self.InSimVer = InSimVer
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, str_factory.encode(self.Version), str_factory.encode(self.Product), self.InSimVer)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Version, self.Product, self.InSimVer = self.s.unpack(data)
        self.Version = str_factory.decode(self.Version)
        self.Product = str_factory.decode(self.Product)
        return self

# State Flags
ISS_NONE = 0
ISS_GAME = 1
ISS_REPLAY = 2
ISS_PAUSED = 4
ISS_SHIFTU = 8
ISS_16 = 16
ISS_SHIFTU_FOLLOW = 32
ISS_SHIFTU_NO_OPT = 64
ISS_SHOW_2D = 128
ISS_FRONT_END = 256
ISS_MULTI = 512
ISS_MPSPEEDUP = 1024
ISS_WINDOWED = 2048
ISS_SOUND_MUTE = 4096
ISS_VIEW_OVERRIDE = 8192
ISS_VISIBLE = 16384

# STA InGameCam and CCH Camera
VIEW_FOLLOW = 0
VIEW_HELI = 1
VIEW_CAM = 2
VIEW_DRIVER = 3
VIEW_CUSTOM = 5
VIEW_ANOTHER = 255

class IS_STA:
    """STAte"""
    s = struct.Struct('3BxfH8B2x5sx2B')
    def __init__(self, ReqI=0, ReplaySpeed=0.0, Flags=ISS_NONE, InGameCam=VIEW_FOLLOW, ViewPLID=0, NumP=0, NumConns=0, NumFinished=0, RaceInProg=0, QualMins=0, RaceLaps=0, Track='', Weather=0, Wind=0):
        self.Size = 28
        self.Type = ISP_STA
        self.ReqI = ReqI
        self.ReplaySpeed = ReplaySpeed
        self.Flags = Flags
        self.InGameCam = InGameCam
        self.ViewPLID = ViewPLID
        self.NumP = NumP
        self.NumConns = NumConns
        self.NumFinished = NumFinished
        self.RaceInProg = RaceInProg
        self.QualMins = QualMins
        self.RaceLaps = RaceLaps
        self.Track = Track
        self.Weather = Weather
        self.Wind = Wind
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.ReplaySpeed, self.Flags, self.InGameCam, self.ViewPLID, self.NumP, self.NumConns, self.NumFinished, self.RaceInProg, self.QualMins, self.RaceLaps, str_factory.encode(self.Track), self.Weather, self.Wind)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.ReplaySpeed, self.Flags, self.InGameCam, self.ViewPLID, self.NumP, self.NumConns, self.NumFinished, self.RaceInProg, self.QualMins, self.RaceLaps, self.Track, self.Weather, self.Wind = self.s.unpack(data)
        self.Track = str_factory.decode(self.Track)
        return self

class IS_SFP:
    """State Flags Pack"""
    s = struct.Struct('3BxHBx')
    def __init__(self, ReqI=0, Flag=ISS_NONE, OffOn=0):
        self.Size = 8
        self.Type = ISP_SFP
        self.ReqI = ReqI
        self.Flag = Flag
        self.OffOn = OffOn
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.Flag, self.OffOn)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Flag, self.OffOn = self.s.unpack(data)
        return self

class IS_MOD:
    """MODe : send to LFS to change screen mode"""
    s = struct.Struct('3Bx4i')
    def __init__(self, ReqI=0, Bits16=0, RR=0, Width=0, Height=0):
        self.Size = 20
        self.Type = ISP_MOD
        self.ReqI = ReqI
        self.Bits16 = Bits16
        self.RR = RR
        self.Width = Width
        self.Height = Height
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.Bits16, self.RR, self.Width, self.Height)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Bits16, self.RR, self.Width, self.Height = self.s.unpack(data)
        return self

# MSO UserType
MSO_SYSTEM = 0
MSO_USER = 1
MSO_PREFIX = 2
MSO_O = 3

class IS_MSO:
    """MSg Out - system messages and user messages"""
    s = struct.Struct('3Bx4B127sx')
    def __init__(self, ReqI=0, UCID=0, PLID=0, UserType=MSO_SYSTEM, TextStart=0, Msg=''):
        self.Size = 136
        self.Type = ISP_MSO
        self.ReqI = ReqI
        self.UCID = UCID
        self.PLID = PLID
        self.UserType = UserType
        self.TextStart = TextStart
        self.Msg = Msg
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, self.PLID, self.UserType, self.TextStart, str_factory.encode(self.Msg))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.PLID, self.UserType, self.TextStart, self.Msg = self.s.unpack(data)
        self.Msg = str_factory.decode(self.Msg)
        return self

class IS_III:
    """InsIm Info - /i message from user to host's InSim"""
    s = struct.Struct('3Bx2B2x63sx')
    def __init__(self, ReqI=0, UCID=0, PLID=0, Msg=''):
        self.Size = 72
        self.Type = ISP_III
        self.ReqI = ReqI
        self.UCID = UCID
        self.PLID = PLID
        self.Msg = Msg
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, self.PLID, str_factory.encode(self.Msg))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.PLID, self.Msg = self.s.unpack(data)
        self.Msg = str_factory.decode(self.Msg)
        return self

class IS_ACR:
    """Admin Command Report - any user typed an admin command"""
    s = struct.Struct('3Bx3Bx63sx')
    def __init__(self, ReqI=0, UCID=0, Admin=0, Result=0, Text=''):
        self.Size = 72
        self.Type = ISP_ACR
        self.ReqI = ReqI
        self.UCID = UCID
        self.Admin = Admin
        self.Result = Result
        self.Text = Text
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, self.Admin, self.Result, str_factory.encode(self.Text))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.Admin, self.Result, self.Text = self.s.unpack(data)
        self.Text = str_factory.decode(self.Text)
        return self

class IS_MST:
    """MSg Type - send to LFS to type message or command"""
    s = struct.Struct('3Bx63sx')
    def __init__(self, ReqI=0, Msg=''):
        self.Size = 68
        self.Type = ISP_MST
        self.ReqI = ReqI
        self.Msg = Msg
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, str_factory.encode(self.Msg))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Msg = self.s.unpack(data)
        self.Msg = str_factory.decode(self.Msg)
        return self

class IS_MSX:
    """MSg eXtended - like MST but longer (not for commands)"""
    s = struct.Struct('3Bx95sx')
    def __init__(self, ReqI=0, Msg=''):
        self.Size = 100
        self.Type = ISP_MSX
        self.ReqI = ReqI
        self.Msg = Msg
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, str_factory.encode(self.Msg))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Msg = self.s.unpack(data)
        self.Msg = str_factory.decode(self.Msg)
        return self

# MSL and MTC Sound.
SND_SILENT = 0
SND_MESSAGE = 1
SND_SYSMESSAGE = 2
SND_INVALIDKEY = 3
SND_ERROR = 4

class IS_MSL:
    """MSg Local - message to appear on local computer only"""
    s = struct.Struct('4B127sx')
    def __init__(self, ReqI=0, Sound=SND_SILENT, Msg=''):
        self.Size = 132
        self.Type = ISP_MSL
        self.ReqI = ReqI
        self.Sound = Sound
        self.Msg = Msg
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.Sound, str_factory.encode(self.Msg))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Sound, self.Msg = self.s.unpack(data)
        self.Msg = str_factory.decode(self.Msg)
        return self

class IS_MTC:
    """Msg To Connection - hosts only - send to a connection / a player / all"""
    s = struct.Struct('6B2x')
    def __init__(self, ReqI=0, Sound=SND_SILENT, UCID=0, PLID=0, Text=''):
        self.Size = 8
        self.Type = ISP_MTC
        self.ReqI = ReqI
        self.Sound = Sound
        self.UCID = UCID
        self.PLID = PLID
        self.Text = Text
    def pack(self):
        text = str_factory.encode(self.Text)
        text_size = len(text) + 4 - (len(text) % 4)
        return self.s.pack(self.Size + text_size, self.Type, self.ReqI, self.Sound, self.UCID, self.PLID) + struct.pack('{0}s'.format(text_size), text)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Sound, self.UCID, self.PLID = self.s.unpack(data[:8])
        self.Text = struct.unpack('{0}s'.format(self.Size - 8), data[8:])[0]
        self.Text = str_factory.decode(self.Text)
        return self

class IS_SCH:
    """Single CHaracter"""
    s = struct.Struct('3BxcB2x')
    def __init__(self, ReqI=0, CharB=0, Flags=0):
        self.Size = 8
        self.Type = ISP_SCH
        self.ReqI = ReqI
        self.CharB = CharB
        self.Flags = Flags
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, str_factory.encode(self.CharB), self.Flags)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.CharB, self.Flags = self.s.unpack(data)
        return self

class IS_ISM:
    """InSim Multi"""
    s = struct.Struct('3BxB3x31sx')
    def __init__(self, ReqI=0, Host=0, HName=''):
        self.Size = 40
        self.Type = ISP_ISM
        self.ReqI = ReqI
        self.Host = Host
        self.HName = HName
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.Host, str_factory.encode(self.HName))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Host, self.HName = self.s.unpack(data)
        self.HName = str_factory.decode(self.HName)
        return self

# VTN Action
VOTE_NONE = 0
VOTE_END = 1
VOTE_RESTART = 2
VOTE_QUALIFY = 3

class IS_VTN:
    """VoTe Notify"""
    s = struct.Struct('3Bx2B2x')
    def __init__(self, ReqI=0, UCID=0, Action=VOTE_NONE):
        self.Size = 8
        self.Type = ISP_VTN
        self.ReqI = ReqI
        self.UCID = UCID
        self.Action = Action
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, self.Action)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.Action = self.s.unpack(data)
        return self

# PLC Cars
CAR_NONE = 0
CAR_XFG = 1
CAR_XRG = 2
CAR_XRT = 4
CAR_RB4 = 8
CAR_FXO = 0x10
CAR_LX4 = 0x20
CAR_LX6 = 0x40
CAR_MRT = 0x80
CAR_UF1 = 0x100
CAR_RAC = 0x200
CAR_FZ5 = 0x400
CAR_FOX = 0x800
CAR_XFR = 0x1000
CAR_UFR = 0x2000
CAR_FO8 = 0x4000
CAR_FXR = 0x8000
CAR_XRR = 0x10000
CAR_FZR = 0x20000
CAR_BF1 = 0x40000
CAR_FBM = 0x80000
CAR_ALL = 0xffffffff

class IS_PLC:
    """PLayer Cars"""
    s = struct.Struct('3BxB3xI')
    def __init__(self, ReqI=0, UCID=0, Cars=CAR_NONE):
        self.Size = 12
        self.Type = ISP_PLC
        self.ReqI = ReqI
        self.UCID = UCID
        self.Cars = Cars
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, self.Cars)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.Cars = self.s.unpack(data)
        return self

class IS_RST:
    """Race STart"""
    s = struct.Struct('3Bx4B5sx2B6H')
    def __init__(self, ReqI=0, RaceLaps=0, QualMins=0, NumP=0, Timing=0, Track='', Weather=0, Wind=0, Flags=0, NumNodes=0, Finish=0, Split1=0, Split2=0, Split3=0):
        self.Size = 28
        self.Type = ISP_RST
        self.ReqI = ReqI
        self.RaceLaps = RaceLaps
        self.QualMins = QualMins
        self.NumP = NumP
        self.Timing = Timing
        self.Track = Track
        self.Weather = Weather
        self.Wind = Wind
        self.Flags = Flags
        self.NumNodes = NumNodes
        self.Finish = Finish
        self.Split1 = Split1
        self.Split2 = Split2
        self.Split3 = Split3
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.RaceLaps, self.QualMins, self.NumP, self.Timing, str_factory.encode(self.Track), self.Weather, self.Wind, self.Flags, self.NumNodes, self.Finish, self.Split1, self.Split2, self.Split3)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.RaceLaps, self.QualMins, self.NumP, self.Timing, self.Track, self.Weather, self.Wind, self.Flags, self.NumNodes, self.Finish, self.Split1, self.Split2, self.Split3 = self.s.unpack(data)
        self.Track = str_factory.decode(self.Track)
        return self

# NCN Flags
HOSTF_NONE = 0
HOSTF_CAN_VOTE = 1
HOSTF_CAN_SELECT = 2
HOSTF_MID_RACE = 32
HOSTF_MUST_PIT = 64
HOSTF_CAN_RESET  = 128
HOSTF_FCV = 256
HOSTF_CRUISE = 512

class IS_NCN:
    """New ConN"""
    s = struct.Struct('4B23sx23sx3Bx')
    def __init__(self, ReqI=0, UCID=0, UName='', PName='', Admin=0, Total=0, Flags=HOSTF_NONE):
        self.Size = 56
        self.Type = ISP_NCN
        self.ReqI = ReqI
        self.UCID = UCID
        self.UName = UName
        self.PName = PName
        self.Admin = Admin
        self.Total = Total
        self.Flags = Flags
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, str_factory.encode(self.UName), str_factory.encode(self.PName), self.Admin, self.Total, self.Flags)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.UName, self.PName, self.Admin, self.Total, self.Flags = self.s.unpack(data)
        self.UName = str_factory.decode(self.UName)
        self.PName = str_factory.decode(self.PName)
        return self

# CNL Reason.
LEAVR_DISCO = 0
LEAVR_TIMEOUT = 1
LEAVR_LOSTCONN = 2
LEAVR_KICKED = 3
LEAVR_BANNED = 4
LEAVR_SECURITY = 5

class IS_CNL:
    """ConN Leave"""
    s = struct.Struct('6B2x')
    def __init__(self, ReqI=0, UCID=0, Reason=LEAVR_DISCO, Total=0):
        self.Size = 8
        self.Type = ISP_CNL
        self.ReqI = ReqI
        self.UCID = UCID
        self.Reason = Reason
        self.Total = Total
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, self.Reason, self.Total)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.Reason, self.Total = self.s.unpack(data)
        return self

class IS_CPR:
    """Conn Player Rename"""
    s = struct.Struct('4B23sx8s')
    def __init__(self, ReqI=0, UCID=0, PName='', Plate=''):
        self.Size = 36
        self.Type = ISP_CPR
        self.ReqI = ReqI
        self.UCID = UCID
        self.PName = PName
        self.Plate = Plate
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, str_factory.encode(self.PName), str_factory.encode(self.Plate))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.PName, self.Plate = self.s.unpack(data)
        self.PName = str_factory.decode(self.PName)
        self.Plate = str_factory.decode(self.Plate)
        return self

# NPL SetF
SETF_NONE = 0
SETF_SYMM_WHEELS = 1
SETF_TC_ENABLE = 2
SETF_ABS_ENABLE = 4

# LAP, PIT and NPL Flags
PIF_NONE = 0
PIF_SWAPSIDE = 1
PIF_RESERVED_2 = 2
PIF_RESERVED_4 = 4
PIF_AUTOGEARS = 8
PIF_SHIFTER = 16
PIF_RESERVED_32 = 32
PIF_HELP_B = 64
PIF_AXIS_CLUTCH = 128
PIF_INPITS = 256
PIF_AUTOCLUTCH = 512
PIF_MOUSE = 1024
PIF_KB_NO_HELP = 2048
PIF_KB_STABILISED = 4096
PIF_CUSTOM_VIEW = 8192

# NPL Tyres
TYRE_R1 = 0
TYRE_R2 = 1
TYRE_R3 = 2
TYRE_R4 = 3
TYRE_ROAD_SUPER = 4
TYRE_ROAD_NORMAL = 5
TYRE_HYBRID = 6
TYRE_KNOBBLY = 7
TYRE_NOT_CHANGED = 255

class IS_NPL:
    """New PLayer joining race (if PLID already exists, then leaving pits)"""
    s = struct.Struct('6BH23sx8s3sx15sx8B4x2B2x')
    def __init__(self, ReqI=0, PLID=0, UCID=0, PType=0, Flags=PIF_NONE, PName='', Plate='', CName='', SName='', Tyres=[TYRE_R1,TYRE_R1,TYRE_R1,TYRE_R1], H_Mass=0, H_TRes=0, Model=0, Pass=0, SetF=SETF_NONE, NumP=0):
        self.Size = 76
        self.Type = ISP_NPL
        self.ReqI = ReqI
        self.PLID = PLID
        self.UCID = UCID
        self.PType = PType
        self.Flags = Flags
        self.PName = PName
        self.Plate = Plate
        self.CName = CName
        self.SName = SName
        self.Tyres = Tyres
        self.H_Mass = H_Mass
        self.H_TRes = H_TRes
        self.Model = Model
        self.Pass = Pass
        self.SetF = SetF
        self.NumP = NumP
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.UCID, self.PType, self.Flags, str_factory.encode(self.PName), str_factory.encode(self.Plate), str_factory.encode(self.CName), str_factory.encode(self.SName), self.Tyres[0], self.Tyres[1], self.Tyres[2], self.Tyres[3], self.H_Mass, self.H_TRes, self.Model, self.Pass, self.SetF, self.NumP)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.UCID, self.PType, self.Flags, self.PName, self.Plate, self.CName, self.SName, self.Tyres[0], self.Tyres[1], self.Tyres[2], self.Tyres[3], self.H_Mass, self.H_TRes, self.Model, self.Pass, self.SetF, self.NumP = self.s.unpack(data)
        self.PName = str_factory.decode(self.PName)
        self.Plate = str_factory.decode(self.Plate)
        self.CName = str_factory.decode(self.CName)
        self.SName = str_factory.decode(self.SName)
        return self

class IS_PLP:
    """PLayer Pits (go to settings - stays in player list)"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, PLID=0):
        self.Size = 4
        self.Type = ISP_PLP
        self.ReqI = ReqI
        self.PLID = PLID
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID = self.s.unpack(data)
        return self

class IS_PLL:
    """PLayer Leave race (spectate - removed from player list)"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, PLID=0):
        self.Size = 4
        self.Type = ISP_PLL
        self.ReqI = ReqI
        self.PLID = PLID
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID = self.s.unpack(data)
        return self

class IS_CRS:
    """Car ReSet"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, PLID=0):
        self.Size = 4
        self.Type = ISP_CRS
        self.ReqI = ReqI
        self.PLID = PLID
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID = self.s.unpack(data)
        return self

# LAP, PIT and SPX Penalty.
PENALTY_NONE = 0        
PENALTY_DT = 1
PENALTY_DT_VALID = 2
PENALTY_SG = 3
PENALTY_SG_VALID = 4
PENALTY_30 = 5
PENALTY_45 = 6

class IS_LAP:
    """LAP time"""
    s = struct.Struct('4B2I2Hx2Bx')
    def __init__(self, ReqI=0, PLID=0, LTime=0, ETime=0, LapsDone=0, Flags=PIF_NONE, Penalty=PENALTY_NONE, NumStops=0):
        self.Size = 20
        self.Type = ISP_LAP
        self.ReqI = ReqI
        self.PLID = PLID
        self.LTime = LTime
        self.ETime = ETime
        self.LapsDone = LapsDone
        self.Flags = Flags
        self.Penalty = Penalty
        self.NumStops = NumStops
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.LTime, self.ETime, self.LapsDone, self.Flags, self.Penalty, self.NumStops)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.LTime, self.ETime, self.LapsDone, self.Flags, self.Penalty, self.NumStops = self.s.unpack(data)
        return self

class IS_SPX:
    """SPlit X time"""
    s = struct.Struct('4B2I3Bx')
    def __init__(self, ReqI=0, PLID=0, STime=0, ETime=0, Split=0, Penalty=PENALTY_NONE, NumStops=0):
        self.Size = 16
        self.Type = ISP_SPX
        self.ReqI = ReqI
        self.PLID = PLID
        self.STime = STime
        self.ETime = ETime
        self.Split = Split
        self.Penalty = Penalty
        self.NumStops = NumStops
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.STime, self.ETime, self.Split, self.Penalty, self.NumStops)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.STime, self.ETime, self.Split, self.Penalty, self.NumStops = self.s.unpack(data)
        return self

# PIT Work.
PSE_NONE = 0
PSE_NOTHING = 1
PSE_STOP = 2
PSE_FR_DAM = 4
PSE_FR_WHL = 8
PSE_LE_FR_DAM = 16
PSE_LE_FR_WHL = 32
PSE_RI_FR_DAM = 64
PSE_RI_FR_WHL = 128
PSE_RE_DAM = 256
PSE_RE_WHL = 512
PSE_LE_RE_DAM = 1024
PSE_LE_RE_WHL = 2048
PSE_RI_RE_DAM = 4096
PSE_RI_RE_WHL = 8192
PSE_BODY_MINOR = 16384
PSE_BODY_MAJOR = 32768
PSE_SETUP = 65536
PSE_REFUEL = 131072

class IS_PIT:
    """PIT stop (stop at pit garage)"""
    s = struct.Struct('4B2Hx2Bx4BI4x')
    def __init__(self, ReqI=0, PLID=0, LapsDone=0, Flags=PIF_NONE, Penalty=PENALTY_NONE, NumStops=0, Tyres=[TYRE_R1,TYRE_R1,TYRE_R1,TYRE_R1], Work=PSE_NONE):
        self.Size = 24
        self.Type = ISP_PIT
        self.ReqI = ReqI
        self.PLID = PLID
        self.LapsDone = LapsDone
        self.Flags = Flags
        self.Penalty = Penalty
        self.NumStops = NumStops
        self.Tyres = Tyres
        self.Work = Work
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.LapsDone, self.Flags, self.Penalty, self.NumStops, self.Tyres[0], self.Tyres[1], self.Tyres[2], self.Tyres[3], self.Work)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.LapsDone, self.Flags, self.Penalty, self.NumStops,  self.Tyres[0], self.Tyres[1], self.Tyres[2], self.Tyres[3], self.Work = self.s.unpack(data)
        return self

class IS_PSF:
    """Pit Stop Finished"""
    s = struct.Struct('4BI4x')
    def __init__(self, ReqI=0, PLID=0, STime=0):
        self.Size = 12
        self.Type = ISP_PSF
        self.ReqI = ReqI
        self.PLID = PLID
        self.STime = STime
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.STime)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.STime = self.s.unpack(data)
        return self

# PLA Fact
PITLANE_EXIT = 0
PITLANE_ENTER = 1
PITLANE_NO_PURPOSE = 2
PITLANE_DT = 3
PITLANE_SG = 4

class IS_PLA:
    """Pit LAne"""
    s = struct.Struct('5B3x')
    def __init__(self, ReqI=0, PLID=0, Fact=PITLANE_EXIT):
        self.Size = 8
        self.Type = ISP_PLA
        self.ReqI = ReqI
        self.PLID = PLID
        self.Fact = Fact
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.Fact)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.Fact = self.s.unpack(data)
        return self

class IS_CCH:
    """Camera CHange"""
    s = struct.Struct('5B3x')
    def __init__(self, ReqI=0, PLID=0, Camera=VIEW_FOLLOW):
        self.Size = 8
        self.Type = ISP_CCH
        self.ReqI = ReqI
        self.PLID = PLID
        self.Camera = Camera
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.Camera)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.Camera = self.s.unpack(data)
        return self

# PEN Reason.
PENR_UNKNOWN = 0
PENR_ADMIN = 1
PENR_WRONG_WAY = 2
PENR_FALSE_START = 3
PENR_SPEEDING = 4
PENR_STOP_SHORT = 5
PENR_STOP_LATE = 6

class IS_PEN:
    """PENalty (given or cleared)"""
    s = struct.Struct('7Bx')
    def __init__(self, ReqI=0, PLID=0, OldPen=PENALTY_NONE, NewPen=PENALTY_NONE, Reason=PENR_UNKNOWN):
        self.Size = 8
        self.Type = ISP_PEN
        self.ReqI = ReqI
        self.PLID = PLID
        self.OldPen = OldPen
        self.NewPen = NewPen
        self.Reason = Reason
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.OldPen, self.NewPen, self.Reason)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.OldPen, self.NewPen, self.Reason = self.s.unpack(data)
        return self

class IS_TOC:
    """Take Over Car"""
    s = struct.Struct('6B2x')
    def __init__(self, ReqI=0, PLID=0, OldUCID=0, NewUCID=0):
        self.Size = 8
        self.Type = ISP_TOC
        self.ReqI = ReqI
        self.PLID = PLID
        self.OldUCID = OldUCID
        self.NewUCID = NewUCID
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.OldUCID, self.NewUCID)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.OldUCID, self.NewUCID = self.s.unpack(data)
        return self

class IS_FLG:
    """FLaG (yellow or blue flag changed)"""
    s = struct.Struct('7Bx')
    def __init__(self, ReqI=0, PLID=0, OffOn=0, Flag=0, CarBehind=0):
        self.Size = 8
        self.Type = ISP_FLG
        self.ReqI = ReqI
        self.PLID = PLID
        self.OffOn = OffOn
        self.Flag = Flag
        self.CarBehind = CarBehind
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.OffOn, self.Flag, self.CarBehind)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.OffOn, self.Flag, self.CarBehind = self.s.unpack(data)
        return self

class IS_PFL:
    """Player FLags (help flags changed)"""
    s = struct.Struct('4BH2x')
    def __init__(self, ReqI=0, PLID=0, Flags=PIF_NONE):
        self.Size = 8
        self.Type = ISP_PFL
        self.ReqI = ReqI
        self.PLID = PLID
        self.Flags = Flags
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.Flags)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.Flags = self.s.unpack(data)
        return self

# FIN Confirm
CONF_NONE = 0
CONF_MENTIONED = 1
CONF_CONFIRMED = 2
CONF_PENALTY_DT = 4
CONF_PENALTY_SG = 8
CONF_PENALTY_30 = 16
CONF_PENALTY_45 = 32
CONF_DID_NOT_PIT = 64
CONF_DISQ =  (CONF_PENALTY_DT | CONF_PENALTY_SG | CONF_DID_NOT_PIT)
CONF_TIME = (CONF_PENALTY_30 | CONF_PENALTY_45)

class IS_FIN:
    """FINished race notification (not a final result - use IS_RES)"""
    s = struct.Struct('4B2Ix2Bx2H')
    def __init__(self, ReqI=0, PLID=0, TTime=0, BTime=0, NumStops=0, Confirm=CONF_NONE, LapsDone=0, Flags=PIF_NONE):
        self.Size = 20
        self.Type = ISP_FIN
        self.ReqI = ReqI
        self.PLID = PLID
        self.TTime = TTime
        self.BTime = BTime
        self.NumStops = NumStops
        self.Confirm = Confirm
        self.LapsDone = LapsDone
        self.Flags = Flags
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.TTime, self.BTime, self.NumStops, self.Confirm, self.LapsDone, self.Flags)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.TTime, self.BTime, self.NumStops, self.Confirm, self.LapsDone, self.Flags = self.s.unpack(data)
        return self

class IS_RES:
    """RESult (qualify or confirmed finish)"""
    s = struct.Struct('4B23sx23sx8s3sx2Ix2Bx2H2Bh')
    def __init__(self, ReqI=0, PLID=0, UName='', PName='', Plate='', CName='', TTime=0, BTime=0, NumStops=0, Confirm=CONF_NONE, LapsDone=0, Flags=PIF_NONE, ResultNum=0, NumRes=0, PSeconds=0):
        self.Size = 84
        self.Type = ISP_RES
        self.ReqI = ReqI
        self.PLID = PLID
        self.UName = UName
        self.PName = PName
        self.Plate = Plate
        self.CName = CName
        self.TTime = TTime
        self.BTime = BTime
        self.NumStops = NumStops
        self.Confirm = Confirm
        self.LapsDone = LapsDone
        self.Flags = Flags
        self.ResultNum = ResultNum
        self.NumRes = NumRes
        self.PSeconds = PSeconds
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, str_factory.encode(self.UName), str_factory.encode(self.PName), str_factory.encode(self.Plate), str_factory.encode(self.CName), self.TTime, self.BTime, self.NumStops, self.Confirm, self.LapsDone, self.Flags, self.ResultNum, self.NumRes, self.PSeconds)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.UName, self.PName, self.Plate, self.CName, self.TTime, self.BTime, self.NumStops, self.Confirm, self.LapsDone, self.Flags, self.ResultNum, self.NumRes, self.PSeconds = self.s.unpack(data)
        self.UName = str_factory.decode(self.UName)
        self.PName = str_factory.decode(self.PName)
        self.Plate = str_factory.decode(self.Plate)
        self.CName = str_factory.decode(self.CName)
        return self

class IS_REO:
    """REOrder (when race restarts after qualifying)"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, NumP=0, PLID=[]):
        self.Size = 36
        self.Type = ISP_REO
        self.ReqI = ReqI
        self.NumP = NumP
        self.PLID = PLID
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.NumP) + struct.pack('{0}B'.format(self.NumP), *self.PLID)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.NumP = self.s.unpack(data[:4])
        self.PLID = [plid for plid in data[4:4+self.NumP]]
        return self

class IS_AXI:
    """AutoX Info"""
    s = struct.Struct('3Bx2BH31sx')
    def __init__(self, ReqI=0, AXStart=0, NumCP=0, NumO=0, LName=''):
        self.Size = 40
        self.Type = ISP_AXI
        self.ReqI = ReqI
        self.AXStart = AXStart
        self.NumCP = NumCP
        self.NumO = NumO
        self.LName = LName
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.AXStart, self.NumCP, self.NumO, str_factory.encode(self.LName))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.AXStart, self.NumCP, self.NumO, self.LName = self.s.unpack(data)
        self.LName = str_factory.decode(self.LName)
        return self

class IS_AXO:
    """AutoX Object"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, PLID=0):
        self.Size = 4
        self.Type = ISP_AXO
        self.ReqI = ReqI
        self.PLID = PLID
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID = self.s.unpack(data)
        return self

class NodeLap:
    """Car info in 6 bytes - there is an array of these in the NLP (below)"""
    s = struct.Struct('2H2B')
    def __init__(self, Node=0, Lap=0, PLID=0, Position=0):
        self.Node = Node
        self.Lap = Lap
        self.PLID = PLID
        self.Position = Position
    def pack(self):
        return self.s.pack(self.Node, self.Lap, self.PLID, self.Position)
    def unpack(self, data):
        self.Node, self.Lap, self.PLID, self.Position = self.s.unpack(data)
        return self

class IS_NLP:
    """Node and Lap Packet - variable size"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, NumP=0, Info=[]):
        self.Size = 4
        self.Type = ISP_NLP
        self.ReqI = ReqI
        self.NumP = NumP
        self.Info = Info
    def pack(self):
        return self.s.pack(self.Size + (self.NumP * 6), self.Type, self.ReqI, self.NumP) + b''.join([info.pack() for info in self.Info])
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.NumP = self.s.unpack(data[:4])
        self.Info = [NodeLap().unpack(data[i:i+6]) for i in range(4, (self.NumP * 6) + 4, 6)]
        return self

# CompCar Info
CCI_NONE   = 0
CCI_BLUE   = 1
CCI_YELLOW = 2
CCI_LAG    = 32
CCI_FIRST  = 64
CCI_LAST   = 128    

class CompCar:
    """Car info in 28 bytes - there is an array of these in the MCI (below)"""
    s = struct.Struct('2H3Bx3i3Hh')
    def __init__(self, Node=0, Lap=0, PLID=0, Position=0, Info=CCI_NONE, X=0, Y=0, Z=0, Speed=0, Direction=0, Heading=0, AngVel=0):
        self.Node = Node
        self.Lap = Lap
        self.PLID = PLID
        self.Position = Position
        self.Info = Info
        self.X = X
        self.Y = Y
        self.Z = Z
        self.Speed = Speed
        self.Direction = Direction
        self.Heading = Heading
        self.AngVel = AngVel
    def pack(self):
        return self.s.pack(self.Node, self.Lap, self.PLID, self.Position, self.Info, self.X, self.Y, self.Z, self.Speed, self.Direction, self.Heading, self.AngVel)
    def unpack(self, data):
        self.Node, self.Lap, self.PLID, self.Position, self.Info, self.X, self.Y, self.Z, self.Speed, self.Direction, self.Heading, self.AngVel = self.s.unpack(data)
        return self

class IS_MCI:
    """Multi Car Info - if more than 8 in race then more than one of these is sent"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, NumC=0, Info=[]):
        self.Size = 4
        self.Type = ISP_MCI
        self.ReqI = ReqI
        self.NumC = NumC
        self.Info = Info
    def pack(self):
        return self.s.pack(self.Size + (self.NumC * 28), self.Type, self.ReqI, self.NumC) + b''.join([info.pack() for info in self.Info])
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.NumC = self.s.unpack(data[:self.Size])
        self.Info = [CompCar().unpack(data[i:i+28]) for i in range(4, (self.NumC * 28) + 4, 28)]
        return self

class CarContact:
    """16 bytes : one car in a contact - two of these in the IS_CON (below)"""
    s = struct.Struct('2Bxb6B2b2h')
    def __init__(self, PLID=0, Info=CCI_NONE, Steer=0, ThrBrk=0, CluHan=0, GearSp=0, Speed=0, Direction=0, Heading=0, AccelF=0, AccelR=0, X=0, Y=0):
        self.PLID = PLID
        self.Info = Info
        self.Steer = Steer
        self.ThrBrk = ThrBrk
        self.CluHan = CluHan
        self.GearSp = GearSp
        self.Speed = Speed
        self.Direction = Direction
        self.Heading = Heading
        self.AccelF = AccelF
        self.AccelR = AccelR
        self.X = X
        self.Y = Y
    def pack(self):
        return self.s.pack(self.PLID, self.Info, self.Steer, self.ThrBrk, self.CluHan, self.GearSp, self.Speed, self.Direction, self.Heading, self.AccelF, self.AccelR, self.X, self.Y)
    def unpack(self, data):
        self.PLID, self.Info, self.Steer, self.ThrBrk, self.CluHan, self.GearSp, self.Speed, self.Direction, self.Heading, self.AccelF, self.AccelR, self.X, self.Y = self.s.unpack(data)
        return self

class IS_CON:
    """CONtact - between two cars (A and B are sorted by PLID)"""
    s = struct.Struct('3Bx2H')
    def __init__(self, ReqI=0, SpClose=0, Time=0, A=None, B=None):
        self.Size = 8
        self.Type = ISP_CON
        self.ReqI = ReqI
        self.SpClose = SpClose
        self.Time = Time
        self.A = A
        self.B = B
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.SpClose, self.Time) + self.A.pack() + self.B.pack()
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.SpClose, self.Time = self.s.unpack(data[:8])
        self.A = CarContact().unpack(data[8:24])
        self.B = CarContact().unpack(data[24:40])
        return self

class CarContOBJ:
    """8 bytes : car in a contact with an object"""
    s = struct.Struct('3Bx2h')
    def __init__(self, Direction=0, Heading=0, Speed=0, X=0, Y=0):
        self.Direction = Direction
        self.Heading = Heading
        self.Speed = Speed
        self.X = X
        self.Y = Y
    def pack(self):
        return self.s.pack(self.Direction, self.Heading, self.Speed, self.X, self.Y)
    def unpack(self, data):
        self.Direction, self.Heading, self.Speed, self.X, self.Y = self.s.unpack(data)
        return self

# OBH OBHFlags
OBH_NONE       = 0
OBH_LAYOUT     = 1
OBH_CAN_MOVE   = 2
OBH_WAS_MOVING = 4
OBH_ON_SPOT    = 8

class IS_OBH:
    """OBject Hit - car hit an autocross object or an unknown object"""
    s = struct.Struct('4B2H8x2h2x2B')
    def __init__(self, ReqI=0, PLID=0, SpClose=0, Time=0, C=None, X=0, Y=0, Index=0, OBHFlags=OBH_NONE):
        self.Size = 16
        self.Type = ISP_OBH
        self.ReqI = ReqI
        self.PLID = PLID
        self.SpClose = SpClose
        self.Time = Time
        self.C = C
        self.X = X
        self.Y = Y
        self.Index = Index
        self.OBHFlags = OBHFlags
    def pack(self):
        data = self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.SpClose, self.Time, self.X, self.Y, self.Index, self.OBHFlags)
        return data[:8] + self.C.pack() + data[16:]
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.SpClose, self.Time, self.X, self.Y, self.Index, self.OBHFlags = self.s.unpack(data)
        self.C = CarContOBJ().unpack(data[8:16])
        return self

class IS_HLV:
    """Hot Lap Validity - illegal ground / hit wall / speeding in pit lane"""
    s = struct.Struct('5BxH')
    def __init__(self, ReqI=0, PLID=0, HLVC=0, Time=0, C=None):
        self.Size = 8
        self.Type = ISP_HLV
        self.ReqI = ReqI
        self.PLID = PLID
        self.HLVC = HLVC
        self.Time = Time
        self.C = C
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.PLID, self.HLVC, self.Time) + self.C.pack()
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.PLID, self.HLVC, self.Time = self.s.unpack(data[:8])
        self.C = CarContOBJ().unpack(data[8:])
        return self

class ObjectInfo:
    """Info about a single object - explained in the layout file format"""
    s = struct.Struct('2hb3B')
    def __init__(self, X=0, Y=0, Zchar=0, Flags=0, Index=0, Heading=0):
        self.X = X
        self.Y = Y
        self.Zchar = Zchar
        self.Flags = Flags
        self.Index = Index
        self.Heading = Heading
    def pack(self):
        return self.s.pack(self.X, self.Y, self.Zchar, self.Flags, self.Index, self.Heading)
    def unpack(self, data):
        self.X, self.Y, self.Zchar, self.Flags, self.Index, self.Heading = self.s.unpack(data)
        return self

# AXM PMOAction.
PMO_LOADING_FILE = 0
PMO_ADD_OBJECTS  = 1
PMO_DEL_OBJECTS  = 2
PMO_CLEAR_ALL    = 3

class IS_AXM:
    """AutoX Multiple objects - variable size"""
    s = struct.Struct('7Bx')
    def __init__(self, ReqI=0, NumO=0, UCID=0, PMOAction=PMO_LOADING_FILE, PMOFlags=0, Info=[]):
        self.Size = 8
        self.Type = ISP_AXM
        self.ReqI = ReqI
        self.NumO = NumO
        self.UCID = UCID
        self.PMOAction = PMOAction
        self.PMOFlags = PMOFlags
        self.Info = Info
    def pack(self):
        return self.s.pack(self.Size + (self.NumO * 8), self.Type, self.ReqI, self.NumO, self.UCID, self.PMOAction, self.PMOFlags) + b''.join([info.pack() for info in self.Info])
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.NumO, self.UCID, self.PMOAction, self.PMOFlags = self.s.unpack(data[:8])
        self.Info = [ObjectInfo().unpack(data[i:i+8]) for i in range(8, (self.NumO * 8) + 8, 8)]
        return self

class IS_SCC:
    """Set Car Camera - Simplified camera packet (not SHIFT+U mode)"""
    s = struct.Struct('3Bx2B2x')
    def __init__(self, ReqI=0, ViewPLID=0, InGameCam=VIEW_FOLLOW):
        self.Size = 8
        self.Type = ISP_SCC
        self.ReqI = ReqI
        self.ViewPLID = ViewPLID
        self.InGameCam = InGameCam
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.ViewPLID, self.InGameCam)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.ViewPLID, self.InGameCam = self.s.unpack(data)
        return self

class IS_CPP:
    """Cam Pos Pack - Full camera packet (in car OR SHIFT+U mode)"""
    s = struct.Struct('3Bx3i3H2Bf2H')
    def __init__(self, ReqI=0, Pos=[0,0,0], H=0, P=0, R=0, ViewPLID=0, InGameCam=VIEW_FOLLOW, FOV=0.0, Time=0, Flags=ISS_NONE):
        self.Size = 32
        self.Type = ISP_CPP
        self.ReqI = ReqI
        self.Pos = Pos
        self.H = H
        self.P = P
        self.R = R
        self.ViewPLID = ViewPLID
        self.InGameCam = InGameCam
        self.FOV = FOV
        self.Time = Time
        self.Flags = Flags
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.Pos[0], self.Pos[1], self.Pos[2], self.H, self.P, self.R, self.ViewPLID, self.InGameCam, self.FOV, self.Time, self.Flags)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Pos[0], self.Pos[1], self.Pos[2], self.H, self.P, self.R, self.ViewPLID, self.InGameCam, self.FOV, self.Time, self.Flags = self.s.unpack(data)
        return self

# RIP Error
RIP_OK = 0
RIP_ALREADY = 1
RIP_DEDICATED = 2
RIP_WRONG_MODE = 3
RIP_NOT_REPLAY = 4
RIP_CORRUPTED = 5
RIP_NOT_FOUND = 6
RIP_UNLOADABLE = 7
RIP_DEST_OOB = 8
RIP_UNKNOWN = 9
RIP_USER = 10
RIP_OOS = 11

# RIP Options
RIPOPT_NONE = 0
RIPOPT_LOOP = 1
RIPOPT_SKINS = 2
RIPOPT_FULL_PHYS = 4

class IS_RIP:
    """Replay Information Packet"""
    s = struct.Struct('7Bx2I63sx')
    def __init__(self, ReqI=0, Error=RIP_OK, MPR=0, Paused=0, Options=RIPOPT_NONE, CTime=0, TTime=0, RName=''):
        self.Size = 80
        self.Type = ISP_RIP
        self.ReqI = ReqI
        self.Error = Error
        self.MPR = MPR
        self.Paused = Paused
        self.Options = Options
        self.CTime = CTime
        self.TTime = TTime
        self.RName = RName
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.Error, self.MPR, self.Paused, self.Options, self.CTime, self.TTime, str_factory.encode(self.RName))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Error, self.MPR, self.Paused, self.Options, self.CTime, self.TTime, self.RName = self.s.unpack(data)
        self.RName = str_factory.decode(self.RName)
        return self

# SSH Error
SSH_OK = 0
SSH_DEDICATED = 1
SSH_CORRUPTED = 2
SSH_NO_SAVE = 3

class IS_SSH:
    """ScreenSHot"""
    s = struct.Struct('4B2x31sx')
    def __init__(self, ReqI=0, Error=SSH_OK, BMP=''):
        self.Size = 40
        self.Type = ISP_SSH
        self.ReqI = ReqI
        self.Error = Error
        self.BMP = BMP
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.Error, str_factory.encode(self.BMP))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Error, self.BMP = self.s.unpack(data)
        self.BMP = str_factory.decode(self.BMP)
        return self

# Recommended button area
IS_X_MIN = 0
IS_X_MAX = 110
IS_Y_MIN = 30
IS_Y_MAX = 170

# BFN SubT
BFN_DEL_BTN = 0
BFN_CLEAR = 1
BFN_USER_CLEAR = 2
BFN_REQUEST = 3    

# Inst byte
INST_ALWAYS_ON = 128    

class IS_BFN:
    """Button FunctioN - delete buttons / receive button requests"""
    s = struct.Struct('7Bx')
    def __init__(self, ReqI=0, SubT=BFN_DEL_BTN, UCID=0, ClickID=0, Inst=0):
        self.Size = 8
        self.Type = ISP_BFN
        self.ReqI = ReqI
        self.SubT = SubT
        self.UCID = UCID
        self.ClickID = ClickID
        self.Inst = Inst
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.SubT, self.UCID, self.ClickID, self.Inst)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.SubT, self.UCID, self.ClickID, self.Inst = self.s.unpack(data)
        return self

# BTN BStyle colours
ISB_LIGHT_GREY = 0
ISB_TITLE_COLOUR = 1
ISB_UNSELECTED_TEXT = 2
ISB_SELECTED_TEXT = 3
ISB_OK = 4
ISB_CANCEL = 5
ISB_TEXT_STRING = 6
ISB_UNAVAILABLE = 7

# BTN BStyle.
ISB_CLICK = 8
ISB_LIGHT = 16
ISB_DARK = 32
ISB_LEFT = 64
ISB_RIGHT = 128

class IS_BTN:
    """BuTtoN - button header - followed by 0 to 240 characters"""
    s = struct.Struct('12B')
    def __init__(self, ReqI=0, UCID=0, ClickID=0, Inst=0, BStyle=ISB_LIGHT_GREY, TypeIn=0, L=0, T=0, W=0, H=0, Text=''):
        self.Size = 12
        self.Type = ISP_BTN
        self.ReqI = ReqI
        self.UCID = UCID
        self.ClickID = ClickID
        self.Inst = Inst
        self.BStyle = BStyle
        self.TypeIn = TypeIn
        self.L = L
        self.T = T
        self.W = W
        self.H = H
        self.Text = Text
    def pack(self):
        text = str_factory.encode(self.Text)
        text_size = len(text) + 4 - (len(text) % 4)
        return self.s.pack(self.Size + text_size, self.Type, self.ReqI, self.UCID, self.ClickID, self.Inst, self.BStyle, self.TypeIn, self.L, self.T, self.W, self.H) + struct.pack('{0}s'.format(text_size), text)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.ClickID, self.Inst, self.BStyle, self.TypeIn, self.L, self.T, self.W, self.H = self.s.unpack(data[:12])
        self.Text = struct.unpack('{0}s'.format(self.Size - 12), data[12:])[0]
        self.Text = str_factory.decode(self.Text)
        return self

# BTC CFlags
ISB_NONE = 0
ISB_LMB = 1
ISB_RMB = 2
ISB_CTRL = 4
ISB_SHIFT = 8

class IS_BTC:
    """BuTton Click - sent back when user clicks a button"""
    s = struct.Struct('7Bx')
    def __init__(self, ReqI=0, UCID=0, ClickID=0, Inst=0, CFlags=ISB_NONE):
        self.Size = 8
        self.Type = ISP_BTC
        self.ReqI = ReqI
        self.UCID = UCID
        self.ClickID = ClickID
        self.Inst = Inst
        self.CFlags = CFlags
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, self.ClickID, self.Inst, self.CFlags)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.ClickID, self.Inst, self.CFlags = self.s.unpack(data)
        return self

class IS_BTT:
    """BuTton Type - sent back when user types into a text entry button"""
    s = struct.Struct('7Bx95sx')
    def __init__(self, ReqI=0, UCID=0, ClickID=0, Inst=0, TypeIn=0, Sp3=0, Text=''):
        self.Size = 104
        self.Type = ISP_BTT
        self.ReqI = ReqI
        self.UCID = UCID
        self.ClickID = ClickID
        self.Inst = Inst
        self.TypeIn = TypeIn
        self.Text = Text
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.UCID, self.ClickID, self.Inst, self.TypeIn, str_factory.encode(self.Text))
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.UCID, self.ClickID, self.Inst, self.TypeIn, self.Text = self.s.unpack(data)
        self.Text = str_factory.decode(self.Text)
        return self

class OutSimPack:
    """Motion simulator support"""
    s = struct.Struct('I12f4i')
    def __init__(self, Time=0, AngVel=[0.0, 0.0, 0.0], Heading=0.0, Pitch=0.0, Roll=0.0, Accel=[0.0, 0.0, 0.0], Vel=[0.0, 0.0, 0.0], Pos=[0,0,0], ID=0):
        self.Time = Time
        self.AngVel = AngVel
        self.Heading = Heading
        self.Pitch = Pitch
        self.Roll = Roll
        self.Accel = Accel
        self.Vel = Vel
        self.Pos = Pos
        self.ID = ID
    def pack(self):
        return self.s.pack(self.Time, self.AngVel[0], self.AngVel[1], self.AngVel[2], self.Heading, self.Pitch, self.Roll, self.Accel[0], self.Accel[1], self.Accel[2], self.Vel[0], self.Vel[1], self.Vel[2], self.Pos[0], self.Pos[1], self.Pos[2], self.ID)
    def unpack(self, data):
        self.Time, self.AngVel[0], self.AngVel[1], self.AngVel[2], self.Heading, self.Pitch, self.Roll, self.Accel[0], self.Accel[1], self.Accel[2], self.Vel[0], self.Vel[1], self.Vel[2], self.Pos[0], self.Pos[1], self.Pos[2] = self.s.unpack(data[:64])
        if len(data) == 68:
            self.ID = struct.unpack('i', data[64:])
        return self
    
# OutGaugePack Flags
OG_NONE = 0
OG_SHIFT = 1
OG_CTRL = 2
OG_TURBO = 8192
OG_KM = 6384
OG_BAR = 32768

# OutGauge DashLights
DL_NONE = 0
DL_SHIFT = 1
DL_FULLBEAM = 2
DL_HANDBRAKE = 4
DL_PITSPEED = 8
DL_TC = 16
DL_SIGNAL_L = 32
DL_SIGNAL_R = 64
DL_SIGNAL_ANY = 128
DL_OILWARN = 256
DL_BATTERY = 512
DL_ABS = 1024
DL_SPARE = 2048

class OutGaugePack:
    """External dashboard support"""
    s = struct.Struct('I3sxH2B7f2I3f15sx15sx')
    def __init__(self, Time=0, Car='', Flags=OG_NONE, Gear=0, PLID=0, Speed=0.0, RPM=0.0, Turbo=0.0, EngTemp=0.0, Fuel=0.0, OilPressure=0.0, OilTemp=0.0, DashLights=DL_NONE, ShowLights=DL_NONE, Throttle=0.0, Brake=0.0, Clutch=0.0, Display1='', Display2='', ID=0):
        self.Time = Time
        self.Car = Car
        self.Flags = Flags
        self.Gear = Gear
        self.PLID = PLID
        self.Speed = Speed
        self.RPM = RPM
        self.Turbo = Turbo
        self.EngTemp = EngTemp
        self.Fuel = Fuel
        self.OilPressure = OilPressure
        self.OilTemp = OilTemp
        self.DashLights = DashLights
        self.ShowLights = ShowLights
        self.Throttle = Throttle
        self.Brake = Brake
        self.Clutch = Clutch
        self.Display1 = Display1
        self.Display2 = Display2
        self.ID = ID
    def pack(self):
        return self.s.pack(self.Time, self.Car, self.Flags, self.Gear, self.PLID, self.Speed, self.RPM, self.Turbo, self.EngTemp, self.Fuel, self.OilPressure, self.OilTemp, self.DashLights, self.ShowLights, self.Throttle, self.Brake, self.Clutch, str_factory.encode(self.Display1), str_factory.encode(self.Display2), self.ID)
    def unpack(self, data):
        self.Time, self.Car, self.Flags, self.Gear, self.PLID, self.Speed, self.RPM, self.Turbo, self.EngTemp, self.Fuel, self.OilPressure, self.OilTemp, self.DashLights, self.ShowLights, self.Throttle, self.Brake, self.Clutch, self.Display1, self.Display2 = self.s.unpack(data[:92])
        if len(data) == 96:
            self.ID = struct.unpack('i', data[92:])
        self.Car = str_factory.decode(self.Car)
        self.Display1 = str_factory.decode(self.Display1)
        self.Display2 = str_factory.decode(self.Display2)
        return self

# InSim Relay
IRP_ARQ = 250
IRP_ARP = 251
IRP_HLR = 252
IRP_HOS = 253
IRP_SEL = 254
IRP_ERR = 255

class IR_HLR:
    """HostList Request"""
    s = struct.Struct('3Bx')
    def __init__(self, ReqI=0):
        self.Size = 4
        self.Type = IRP_HLR
        self.ReqI = ReqI
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI = self.s.unpack(data)
        return self

# HInfo Flags
HOS_NONE = 0
HOS_SPECPASS = 1
HOS_LICENSED = 2
HOS_S1 = 4
HOS_S2 = 8
HOS_FIRST = 64
HOS_LAST = 128

class HInfo:
    """Sub packet for IR_HOS. Contains host information"""
    s = struct.Struct('32s6s2B')
    def __init__(self, HName='', Track='', Flags=HOS_NONE, NumConns=0):
        self.HName = HName
        self.Track = Track
        self.Flags = Flags
        self.NumConns = NumConns
    def pack(self):
        return self.s.pack(str_factory.encode(self.HName), str_factory.encode(self.Track), self.Flags, self.NumConns)
    def unpack(self, data):
        self.HName, self.Track, self.Flags, self.NumConns = self.s.unpack(data)
        self.HName = str_factory.decode(self.HName)
        self.Track = str_factory.decode(self.Track)
        return self

class IR_HOS:
    """Hostlist (hosts connected to the Relay)"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, NumHosts=0, Info=[]):
        self.Size = 4
        self.Type = IRP_HOS
        self.ReqI = ReqI
        self.NumHosts = NumHosts
        self.Info = Info
    def pack(self):
        return self.s.pack(self.Size + (self.NumHosts * 40), self.Type, self.ReqI, self.NumHosts) + b''.join([info.pack() for info in self.Info])
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.NumHosts = self.s.unpack(data[:4])
        self.Info = [HInfo().unpack(data[i:i+40]) for i in range(4, (self.NumHosts * 40) + 4, 40)]
        return self

class IR_SEL:
    """Relay select - packet to select a host, so relay starts sending you data"""
    s = struct.Struct('3Bx31sx15sx15sx')
    def __init__(self, ReqI=0, HName='', Admin='', Spec=''):
        self.Size = 68
        self.Type = IRP_SEL
        self.ReqI = ReqI
        self.HName = HName
        self.Admin = Admin
        self.Spec = Spec
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, str_factory.encode(self.HName), str_factory.encode(self.Admin), self.Spec)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.HName, self.Admin, self.Spec = self.s.unpack(data)
        self.HName = str_factory.decode(self.HName)
        self.Admin = str_factory.decode(self.Admin)
        self.Spec = str_factory.decode(self.Spec)
        return self

class IR_ARQ:
    """Admin Request"""
    s = struct.Struct('3Bx')
    def __init__(self, ReqI=0):
        self.Size = 4
        self.Type = IRP_ARQ
        self.ReqI = ReqI
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI = self.s.unpack(data)
        return self
    
class IR_ARP:
    """Admin Response"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, Admin=0):
        self.Size = 4
        self.Type = IRP_ARP
        self.ReqI = ReqI
        self.Admin = Admin
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.Admin)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.Admin = self.s.unpack(data)
        return self

# ERR ErrNo
IR_ERR_NONE = 0
IR_ERR_PACKET = 1
IR_ERR_PACKET2 = 2
IR_ERR_HOSTNAME = 3
IR_ERR_ADMIN = 4
IR_ERR_SPEC = 5
IR_ERR_NOSPEC = 6

class IR_ERR:
    """Relay ERRor"""
    s = struct.Struct('4B')
    def __init__(self, ReqI=0, ErrNo=IR_ERR_NONE):
        self.Size = 4
        self.Type = IRP_ERR
        self.ReqI = ReqI
        self.ErrNo = ErrNo
    def pack(self):
        return self.s.pack(self.Size, self.Type, self.ReqI, self.ErrNo)
    def unpack(self, data):
        self.Size, self.Type, self.ReqI, self.ErrNo = self.s.unpack(data)

if __name__ == '__main__':
    pass
    
    
    