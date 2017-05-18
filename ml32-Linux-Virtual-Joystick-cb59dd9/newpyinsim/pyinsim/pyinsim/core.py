#!/usr/bin/env python
#
# core.py - core library module for pyinsim
#
# Copyright 2008-2012 Alex McBride <xandermcbride@gmail.com>
#
# This software may be used and distributed according to the terms of the
# GNU Lesser General Public License version 2 or any later version.
#

# Dependencies.
import asyncore
import socket
import traceback
import threading
import time

# Libraries.
import pyinsim.insim as insim

__all__ = ['Timer', 'EVT_CLOSE', 'EVT_CONNECT', 'EVT_ERROR', 'EVT_OUTGAUGE', 'EVT_OUTSIM', 'EVT_PACKET', 'InSimClient', 'InSimError', 'OutSimClient', 'PYINSIM_VERSION', 'TcpBuffer', 'TcpSocket', 'UdpSocket', 'check_version', 'insim_init', 'make_packet', 'outgauge_init', 'outsim_init', 'relay_init', 'run', 'is_running', 'close_all']

# Constants.
PYINSIM_VERSION = '3.0.0'
TCP_BUFFER_SIZE = 4096
UDP_BUFFER_SIZE = 512
OUTGAUGE_SIZE = (92, 96)
OUTSIM_SIZE = (64, 68)

# pyinsim events.
EVT_CONNECT = 256
EVT_CLOSE = 257
EVT_ERROR = 258
EVT_PACKET = 259
EVT_OUTSIM = 260
EVT_OUTGAUGE = 261

# Packet lookup.
PACKET_MAP = {insim.ISP_ISI: insim.IS_ISI, insim.ISP_VER: insim.IS_VER, insim.ISP_TINY: insim.IS_TINY, insim.ISP_SMALL: insim.IS_SMALL, insim.ISP_STA: insim.IS_STA, 
              insim.ISP_SCH: insim.IS_SCH, insim.ISP_SFP: insim.IS_SFP, insim.ISP_SCC: insim.IS_SCC, insim.ISP_CPP: insim.IS_CPP, insim.ISP_ISM: insim.IS_ISM, 
              insim.ISP_MSO: insim.IS_MSO, insim.ISP_III: insim.IS_III, insim.ISP_MST: insim.IS_MST, insim.ISP_MTC: insim.IS_MTC, insim.ISP_MOD: insim.IS_MOD, 
              insim.ISP_VTN: insim.IS_VTN, insim.ISP_RST: insim.IS_RST, insim.ISP_NCN: insim.IS_NCN, insim.ISP_CNL: insim.IS_CNL, insim.ISP_CPR: insim.IS_CPR, 
              insim.ISP_NPL: insim.IS_NPL, insim.ISP_PLP: insim.IS_PLP, insim.ISP_PLL: insim.IS_PLL, insim.ISP_LAP: insim.IS_LAP, insim.ISP_SPX: insim.IS_SPX, 
              insim.ISP_PIT: insim.IS_PIT, insim.ISP_PSF: insim.IS_PSF, insim.ISP_PLA: insim.IS_PLA, insim.ISP_CCH: insim.IS_CCH, insim.ISP_PEN: insim.IS_PEN, 
              insim.ISP_TOC: insim.IS_TOC, insim.ISP_FLG: insim.IS_FLG, insim.ISP_PFL: insim.IS_PFL, insim.ISP_FIN: insim.IS_FIN, insim.ISP_RES: insim.IS_RES, 
              insim.ISP_REO: insim.IS_REO, insim.ISP_NLP: insim.IS_NLP, insim.ISP_MCI: insim.IS_MCI, insim.ISP_MSX: insim.IS_MSX, insim.ISP_MSL: insim.IS_MSL, 
              insim.ISP_CRS: insim.IS_CRS, insim.ISP_BFN: insim.IS_BFN, insim.ISP_AXI: insim.IS_AXI, insim.ISP_AXO: insim.IS_AXO, insim.ISP_BTN: insim.IS_BTN, 
              insim.ISP_BTC: insim.IS_BTC, insim.ISP_BTT: insim.IS_BTT, insim.ISP_RIP: insim.IS_RIP, insim.ISP_SSH: insim.IS_SSH, insim.ISP_CON: insim.IS_CON, 
              insim.ISP_OBH: insim.IS_OBH, insim.ISP_HLV: insim.IS_HLV, insim.ISP_PLC: insim.IS_PLC, insim.ISP_AXM: insim.IS_AXM, insim.ISP_ACR: insim.IS_ACR, 
              insim.IRP_ARQ: insim.IR_ARQ, insim.IRP_ARP: insim.IR_ARP, insim.IRP_HLR: insim.IR_HLR, insim.IRP_HOS: insim.IR_HOS, insim.IRP_SEL: insim.IR_SEL,  
              insim.IRP_ERR: insim.IR_ERR, EVT_OUTSIM: insim.OutSimPack, EVT_OUTGAUGE: insim.OutGaugePack}


# Functions.
def build_packet(data, packet_type):
    """Build a packet from the packet data."""
    cls = PACKET_MAP.get(packet_type)
    if cls:
        packet = cls()
        packet.unpack(data)        
        return packet
    return None


def make_packet(packet_type, **kwargs):
    """Make a packet from the packet type and keyword arguments."""
    cls = PACKET_MAP.get(packet_type)
    if cls:
        packet = cls(**kwargs)
        return packet
    return None
        
        
def check_version(version, or_better=True):
    """Determine that the correct version of pyinsim is installed."""
    if or_better and version >= PYINSIM_VERSION:
        return True
    return version == PYINSIM_VERSION
        
        
def insim_init(host='127.0.0.1', port=29999, ReqI=1, UDPPort=0, Flags=0, Prefix='!', Interval=0, Admin='', IName='pyinsim'):
    """Initialise a InSim connection."""
    conn = InSimClient()
    conn.connect(host, port, UDPPort)
    conn.send_packet(insim.IS_ISI(ReqI=ReqI, UDPPort=UDPPort, Flags=Flags, Prefix=Prefix, Interval=Interval, Admin=Admin, IName=IName))
    return conn


def relay_init(host='isrelay.lfs.net', port=47474, ReqI=0, HName='', Admin='', Spec=''):
    """Initialise a InSim Relay connection."""
    conn = InSimClient()
    conn.connect(host, port)
    if HName:
        conn.send_packet(insim.IR_SEL(ReqI=ReqI, HName=HName, Admin=Admin, Spec=Spec))
    return conn
    
    
def outsim_init(host='127.0.0.1', port=30000, callback=None, timeout=30.0):
    """Initialise a OutSim connection."""
    conn = OutSimClient(timeout)
    conn.connect(host, port)
    if callback:
        conn.bind_event(EVT_OUTSIM, callback)
    return conn
    
    
def outgauge_init(host='127.0.0.1', port=30000, callback=None, timeout=30.0):
    """Initialise a OutGauge connection."""
    conn = OutSimClient(timeout)
    conn.connect(host, port)
    if callback:
        conn.bind_event(EVT_OUTGAUGE, callback)
    return conn


class TimerManager:
    """Class to manage pyinsim timers."""
    def __init__(self):
        """Create a new TimerManager class."""
        self.timers = []
        
    def add_timer(self, timer):
        """Add a timer to the timers list."""
        if timer not in self.timers:
            self.timers.append(timer)
            self.force_select_return()
    
    def remove_timer(self, timer):
        """Remove a timer from the list."""
        if timer in self.timers:
            self.timers.remove(timer)
            self.force_select_return()
    
    def force_select_return(self):
        """Hack to make select return."""
        # HACK: In order to update the select timeout we first need to get the
        # select call to return, so we ping LFS to get it to send us some data.
        for s in asyncore.socket_map.values():
            # Make sure we're connected and don't ping on UDP.
            if s.connected and isinstance(s, TcpSocket):
                s.send(insim.IS_TINY(ReqI=1, SubT=insim.TINY_PING).pack())
                break    
    
    def execute_timers(self):
        """Check for elapsed timers and execute their callbacks."""
        time_now = time.time()
        for timer in list(self.timers):
            if timer.has_elapsed(time_now):
                timer.execute_callback()
                if timer.repeat:
                    timer.reset(time_now)
                else:
                    self.remove_timer(timer)
                    
    def get_timeout(self):
        """Get the number of seconds until the next timer is due to elapse."""
        time_now = time.time()
        timeout = None
        for timer in self.timers:
            interval = timer.get_interval(time_now)
            if interval > 0:
                if timeout is None or interval < timeout:
                    timeout = interval
        return timeout        

# Global timer manager.
timer_mgr = TimerManager()


class Timer:
    """Class to represent a non-threaded timer. These timers are executed by 
    the main pyinsim thread."""
    def __init__(self, interval, callback, repeat=False, *args, **kwargs):
        """Create a new timer object."""
        self.interval = interval
        self.callback = callback
        self.repeat = repeat
        self.args = args
        self.kwargs = kwargs
        self.due_time = None

    def start(self):
        """Start the timer."""
        self.reset()
        timer_mgr.add_timer(self)

    def stop(self):
        """Stop the timer."""
        timer_mgr.remove_timer(self)
        
    def reset(self, time_now=None):
        """Reset when the timer is due to elapse."""
        # TODO: combine this with start?
        if not time_now:
            time_now = time.time()
        self.due_time = time_now + self.interval
    
    def has_elapsed(self, time_now):
        """Determine if the timer has elapsed."""
        return time_now >= self.due_time
    
    def get_interval(self, time_now):
        """Determine the number of seconds until the timer is due to elapse."""
        return self.due_time - time_now

    def execute_callback(self):
        """Execute the timer callback function."""
        self.callback(*self.args, **self.kwargs)


def asyncore_loop():
    """Replacement for asyncore.loop() function to add timer support."""
    s_map = asyncore.socket_map
    poll_fun = asyncore.poll

    while s_map:
        timer_mgr.execute_timers()    
    
        timeout = timer_mgr.get_timeout()
              
        poll_fun(timeout, s_map)


def run(background=False):
    """Start the pyinsim event loop. pyinsim will stay in this loop until all 
    connections are closed. Set background to True to run the loop in a 
    seperate thread."""
    if background:
        threading.Thread(target=asyncore_loop).start()
    else:
        asyncore_loop()
        
        
def is_running():
    """Determine if the pyinsim event loop is running."""
    for s in asyncore.socket_map.values():
        if s.connected:
            return True
    return False
    
    
def close_all():
    """Close all current connections and end the event loop."""
    asyncore.close_all()


# Classes.
class InSimError(Exception):
    """Class to represent InSim error."""
    pass
            
               
class TcpBuffer(object):
    """Class to handle TCP receive buffer."""
    def __init__(self):
        """Init new TcpBuffer class."""
        self.buffer = b''
        
    def __iter__(self):
        return self
    
    def __len__(self):
        return len(self.buffer)
        
    def __next__(self):
        """Return next packet in buffer."""
        if self.buffer and len(self) >= self.buffer[0]:
            size = self.buffer[0]
            if size % 4:
                raise InSimError('invalid packet size')
            data = self.buffer[:size]
            self.buffer = self.buffer[size:]
            return data
        raise StopIteration  
    
    def append(self, data):
        """Append data to the buffer."""
        self.buffer += data             
            
             
class TcpSocket(asyncore.dispatcher_with_send):
    """class to handle a TCP socket with LFS."""
    def __init__(self, dispatch_to):
        """Init new TcpSocket object."""
        asyncore.dispatcher_with_send.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.dispatch_to = dispatch_to
        self.recv_buffer = TcpBuffer()
  
    def send(self, data):
        """Send buffer data to LFS."""
        self.out_buffer += data
        if self.connected:
            self.initiate_send()
    
    def handle_connect(self):
        """Handle socket connect event."""
        self.dispatch_to.handle_connect(self)
        
    def handle_close(self):
        """Handle socket close event."""
        self.close()
        self.dispatch_to.handle_close(self)
    
    def handle_read(self):
        """Handle socket read event."""
        data = self.recv(TCP_BUFFER_SIZE)
        if data:
            self.recv_buffer.append(data)
            for data in self.recv_buffer:
                self.dispatch_to.handle_read(self, data)
    
    def handle_error(self):
        """Handle socket error event."""
        self.close()
        self.dispatch_to.handle_error(self)
    
    
class UdpSocket(asyncore.dispatcher):
    """Class to handle a UDP socket with LFS."""
    def __init__(self, dispatch_to):
        """Init a new UdpSocket object."""
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dispatch_to = dispatch_to
        
    def writable(self):
        """Get if the socket is writable."""
        return False
        
    def handle_connect(self):
        """Handle socket connect event."""
        self.dispatch_to.handle_connect(self)
        
    def handle_close(self):
        """Handle socket close event."""
        self.close()
        self.dispatch_to.handle_close(self)
        
    def handle_read(self):
        """Handle socket read event."""
        data = self.recv(UDP_BUFFER_SIZE)
        if data:
            if len(data) % 4:
                raise InSimError('invalid packet size')        
            self.dispatch_to.handle_read(self, data)
            
    def handle_error(self):
        """Handle socket error event."""
        self.close()
        self.dispatch_to.handle_error(self)
           
            
class EventBinding:
    """Class to handle pyinsim events."""
    def __init__(self):
        """Create a new EventBinding object."""
        self.event_bindings = {}
        
    def bind_event(self, event_type, event_callback):
        """Bind a function to be called when an event occurs."""
        callbacks = self.event_bindings.get(event_type)
        if callbacks:
            callbacks.append(event_callback)
        else:
            self.event_bindings[event_type] = [event_callback]
 
    def unbind_event(self, event_type, event_callback):
        """Unbind an event function."""
        callbacks = self.event_bindings.get(event_type)
        if callbacks:
            callbacks.remove(event_callback)
            if not callbacks:
                del self.event_bindings[event_type]
                
    def is_event_bound(self, event_type, event_callback):
        """Determine if an event function is bound."""
        callbacks = self.event_bindings.get(event_type)
        if callbacks:
            return event_callback in callbacks
        return False
 
    def raise_event(self, event_type, *args):
        """Raise an event."""
        callbacks = self.event_bindings.get(event_type)
        if callbacks:
            [c(self, *args) for c in callbacks]
            
    def get_bindings(self, event_type):
        """Get the functions bound to an event."""
        return self.event_bindings.get(event_type, [])
        
    def raise_packet_event(self, packet_type, data):
        """Build a packet and raise an event for it."""
        callbacks = self.get_bindings(packet_type) + self.get_bindings(EVT_PACKET)
        if callbacks:
            # Build packet here so as not to build more packets than necessary.
            packet = build_packet(data, packet_type)
            if callbacks:
                [c(self, packet) for c in callbacks]
                
        
class InSimClient(EventBinding):
    """Class to represent a InSim connection with LFS."""
    def __init__(self):
        """Create a new InSim object."""
        EventBinding.__init__(self)
        self.tcp_socket = TcpSocket(self)
        self.udp_socket = None
        
    def connected(self):
        """Determines if LFS is connected."""
        return self.tcp_socket.connected
        
    def connect(self, host, port, udpport=0):
        """Connect to LFS."""
        self.tcp_socket.connect((host, port))
        if udpport:
            self.udp_socket = UdpSocket(self)
            self.udp_socket.bind((host, udpport))
            
    def close(self):
        """Close the connection with LFS."""
        self.tcp_socket.close()
        if self.udp_socket:
            self.udp_socket.close()        
    
    def send(self, packet_type, **kwargs):
        """Make a packet and send it to LFS"""
        packet = make_packet(packet_type, **kwargs)
        self.tcp_socket.send(packet.pack())
    
    def send_packet(self, packet):
        """Send a packet to LFS."""
        self.tcp_socket.send(packet.pack())
        
    def send_packets(self, packets):
        """Send a sequence of packets to LFS."""
        data = b''.join([p.pack() for p in packets])
        self.tcp_socket.send(data)
        
    def send_message(self, msg, ucid=0, plid=0):
        """Send a message to LFS. The correct message packet will be sent 
        according to the message parameters."""
        if ucid or plid:
            self.tcp_socket.send(insim.IS_MTC(UCID=ucid, PLID=plid, Msg=msg).pack())
        elif len(msg) < 64:
            self.tcp_socket.send(insim.IS_MST(Msg=msg).pack())
        elif len(msg) < 92:
            self.tcp_socket.send(insim.IS_MSX(Msg=msg).pack())
        else:
            raise InSimError("'msg' must contain fewer than 92 chars")
        
    def handle_connect(self, sock):
        """Handle connect event."""
        # Only raise connect for TCP.
        if sock == self.tcp_socket:
            self.raise_event(EVT_CONNECT)
    
    def handle_close(self, sock):
        """Handle close event."""
        self.close()
        self.raise_event(EVT_CLOSE)
    
    def handle_error(self, sock):
        """Handle error event."""
        self.close()
        self.raise_event(EVT_ERROR)
        traceback.print_exc() # Print stacktrace.
       
    def get_packet_type(self, data):
        """Get the type of the packet."""
        return data[1]
       
    def handle_read(self, sock, data):
        """Handle read event."""
        packet_type = self.get_packet_type(data)
        self.handle_internal(packet_type, data)
        self.raise_packet_event(packet_type, data)      
        
    def handle_internal(self, packet_type, data):
        """Handle internal packet events."""
        if packet_type == insim.ISP_TINY:
            if data[3] == insim.TINY_NONE:
                self.tcp_socket.send(data) # Keep alive.
        elif packet_type == insim.ISP_VER:
            ver = build_packet(data, packet_type)
            if ver.InSimVer != insim.INSIM_VERSION:
                raise InSimError('invalid insim version')
             
                                    
class OutSimClient(EventBinding):
    """Class to represent a OutSim or OutGauge connection with LFS."""
    def __init__(self, timeout=None):
        """Create a new OutSim object."""
        EventBinding.__init__(self)
        self.udp_socket = UdpSocket(self)
        # Set timer to handle UDP timeout.
        self.ttimer = None
        if timeout:
            self.ttimer = Timer(timeout, self.handle_timeout)

    def connect(self, host, port):
        """Connect to LFS."""
        self.udp_socket.bind((host, port))
        if self.ttimer:
            self.ttimer.start()
        
    def close(self):
        """Close the connection to LFS."""
        self.udp_socket.close()
        if self.ttimer:
            self.ttimer.stop()           
        
    def handle_connect(self, sock):
        """Handle connect event."""
        self.raise_event(EVT_CONNECT)
    
    def handle_close(self, sock):
        """Handle close event."""
        self.close()
        self.raise_event(EVT_CLOSE)
    
    def handle_error(self, sock):
        """Handle error event."""
        self.close()
        self.raise_event(EVT_ERROR)
        traceback.print_exc()
    
    def get_packet_type(self, data):
        """Get the type of the UDP packet."""
        size = len(data)
        if size in OUTGAUGE_SIZE:
            return EVT_OUTGAUGE
        elif size in OUTSIM_SIZE:
            return EVT_OUTSIM
        return None
    
    def handle_read(self, sock, data):
        """Handle read event."""
        packet_type = self.get_packet_type(data)
        if packet_type and packet_type in (EVT_OUTSIM, EVT_OUTGAUGE):
            # Update timeout due time to account for data received.
            if self.ttimer:
                self.ttimer.reset()
            self.raise_packet_event(packet_type, data)
            
    def handle_timeout(self):
        """Handle timeout event."""
        self.close()
        self.raise_event(EVT_CLOSE)
            
            
if __name__ == '__main__':
    pass

