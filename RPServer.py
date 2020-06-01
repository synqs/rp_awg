#!/usr/bin/env python3
import mmap
import struct
import os
import time
import socket
import sys
import traceback
from JSocket import *

RP_BASEADDRESS = 0x40000000
RP_FPGARAMSIZE = 0x00800000
PORT = 10000
RPVERSION=True

#THIS SCRIPT ASSUMES THAT NGINX AND JUPYTER HAVE BEEN DISABLED, AND THE .bit file installed!
#http://wiki.redpitaya.com/tmp/RedPitaya_HDL_memory_map.pdf

bitfileloaded=False

if RPVERSION:

    fd = os.open('/dev/mem', os.O_RDWR)
    m = mmap.mmap(fileno=fd, length=RP_FPGARAMSIZE, offset=RP_BASEADDRESS)

    #ALL ADDRESSES SHOULD BE SENT LITTLE-ENDIAN!
    #DATA WILL BE WRITTEN INTO MEMORY EXACTLY AS SENT, SO IT IS INCUMENT ON WRITE COMMANDS TO GET THIS CORRECT

# Create a TCP/IP socket & Bind the socket to the port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = (socket.gethostbyname(socket.gethostname()), PORT) # Get real IP Adress and not just hostname
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()
    print(connection)

    if bitfileloaded==False:
        os.system('cat /root/SimonLab_MDDS.bit > /dev/xdevcfg')
        bitfileloaded=True
    try:
        print('connection from', client_address, file=sys.stderr)
        # Receive the data in small chunks and retransmit it
        while True:
            msg=rcv_msg(connection)
            if (msg[1] == 3145728): print('---------------------------------CHANNEL')
            print("\nthe message is:",msg)
            print("dataADDR offset is:" + hex(msg[1]))
            if (msg[0]==b'K'):
                print('okay, then bye....')
                connection.close()
                os.system("fuser -k "+str(PORT)+"/tcp && reboot")
            if (msg[0]==b'Q'):
                break
            if RPVERSION:
                if ((msg[0]==b'w') or (msg[0]==b'W')):
                    for kk in range(int(len(msg[2])/4)):
                        m[msg[1]+4*kk:msg[1]+4*kk+4]=msg[2][4*kk:4*kk+4]
                elif(msg[0]==b'r'):
                    write_msg(connection,0,struct.unpack('<I',m[msg[1]:msg[1]+4])[0])
                    print("the value is:"+str(struct.unpack('<I',m[msg[1]:msg[1]+4])[0]))
                else:
                    print("not implemented!")
            print("")
        print("\n\nclosing")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print('\n',e,traceback.extract_tb(exc_tb)[-1][0], traceback.extract_tb(exc_tb)[-1][1])
        print("Socket Closed Abruptly by Peer")
    finally:
        # Clean up the connection
        print('Finally')
        connection.close()
