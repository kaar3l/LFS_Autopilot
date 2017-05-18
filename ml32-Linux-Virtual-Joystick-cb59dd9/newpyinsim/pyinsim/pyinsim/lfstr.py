#!/usr/bin/env python
#
# insim.py - core library module for pyinsim
#
# Copyright 2008-2012 Alex McBride <xandermcbride@gmail.com>
#
# This software may be used and distributed according to the terms of the
# GNU Lesser General Public License version 2 or any later version.
#

__all__ = ['UniStrFactory', 'AsciiStrFactory', 'StrFactory', 'str_factory']


# Constants.
ENCODING_MAP = {ord('L'): 'cp1252', ord('E'): 'cp1250', ord('T'): 'cp1254', ord('B'): 'cp1257', 
                ord('C'): 'cp1251', ord('G'): 'cp1253', ord('J'): 'cp932',  ord('H'): 'cp950', 
                ord('S'): 'cp936', ord('K'): 'cp949',}
ESCAPE_MAP = {ord('v'): '|', ord('a'): '*', ord('c'): ':', ord('d'): '\\', ord('s'): '/',
              ord('q'): '?', ord('t'): '"', ord('l'): '<', ord('r'): '>', ord('^'): '^',}
DEFAULT_ENCODING = 'cp1252'
CHAR_NULL = 0
CHAR_ESCAPE = ord('^')
ENCODE_FALLBACK = b'?'


class StrFactory:
    def __init__(self):
        pass
        
    def encode(self, unistr):
        pass
    
    def decode(self, lfstr):
        pass


class AsciiStrFactory(StrFactory):
    def __init__(self):
        StrFactory.__init__(self)

    def encode(self, unistr):
        return unistr.encode('ascii', errors='replace')
    
    def decode(self, lfstr):
        return lfstr.decode('ascii', errors='replace').rstrip('\x00')


class UniStrFactory(StrFactory):
    def __init__(self):
        StrFactory.__init__(self)
        
    def encode(self, unistr):
        if len(unistr) == 0:
            return b''
        encoding = DEFAULT_ENCODING
        output = b''
        for c in unistr:
            try:
                output += c.encode(encoding)
            except UnicodeEncodeError:
                found = False
                for esc, cp in ENCODING_MAP.items():
                    if cp != encoding:
                        try:
                            output += b'^' + bytes([esc]) + c.encode(cp)
                        except UnicodeEncodeError:
                            pass
                        else:
                            encoding = cp
                            found = True
                            break
                if not found:
                    output += ENCODE_FALLBACK
        return output
    
    def decode(self, lfstr):
        if len(lfstr) == 0:
            return ''
        encoding = DEFAULT_ENCODING
        output = ''
        i = last_escape = 0
        while i < len(lfstr):
            if lfstr[i] == CHAR_NULL:
                break
            elif lfstr[i]== CHAR_ESCAPE:
                if i - last_escape:
                    output += lfstr[last_escape:i].decode(encoding)
                last_escape = i + 2
                
                cp = ENCODING_MAP.get(lfstr[i+1])
                if cp:
                    encoding = cp
                else:
                    esc = ESCAPE_MAP.get(lfstr[i+1])
                    if esc:
                        output += esc
                    else:
                        output += chr(lfstr[i]) + chr(lfstr[i+1])
                i += 1                
            i += 1
        if i - last_escape:
            output += lfstr[last_escape:i].decode(encoding)  
        return output 


# Get StrFactory used to encode/decode LFS strings.
str_factory = UniStrFactory()


## Functions.
#def lfsdecode(lfstr):
#    """Decode a LFS encoded string to unicode."""
#    if len(lfstr) == 0:
#        return ''
#    encoding = DEFAULT_ENCODING
#    output = ''
#    i = last_escape = 0
#    while i < len(lfstr):
#        if lfstr[i] == CHAR_NULL:
#            break
#        elif lfstr[i]== CHAR_ESCAPE:
#            if i - last_escape:
#                output += lfstr[last_escape:i].decode(encoding)
#            last_escape = i + 2
#            
#            cp = ENCODING_MAP.get(lfstr[i+1])
#            if cp:
#                encoding = cp
#            else:
#                esc = ESCAPE_MAP.get(lfstr[i+1])
#                if esc:
#                    output += esc
#                else:
#                    output += chr(lfstr[i]) + chr(lfstr[i+1])
#            i += 1                
#        i += 1
#    if i - last_escape:
#        output += lfstr[last_escape:i].decode(encoding)  
#    return output
#
#def lfsencode(unistr):
#    """Encode a unicode to a LFS encoded string."""
#    if len(unistr) == 0:
#        return b''
#    encoding = DEFAULT_ENCODING
#    output = b''
#    for c in unistr:
#        try:
#            output += c.encode(encoding)
#        except UnicodeEncodeError:
#            found = False
#            for esc, cp in ENCODING_MAP.items():
#                if cp != encoding:
#                    try:
#                        output += b'^' + bytes([esc]) + c.encode(cp)
#                    except UnicodeEncodeError:
#                        pass
#                    else:
#                        encoding = cp
#                        found = True
#                        break
#            if not found:
#                output += ENCODE_FALLBACK
#    return output
