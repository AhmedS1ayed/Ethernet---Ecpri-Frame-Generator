import struct
import random
import crcmod
from config import configuration
from FCS import FCS

configs = configuration()

src_mac = configs['SOURCE_ADDRESS']
dst_mac = configs['DESTINATION_ADDRESS']
ether_type = configs['ETHER_TYPE']
max_packet_size = configs['MAX_PACKET_SIZE']

with open('packets.txt', 'w') as file:
    for i in range(10):
        preamble = b''.join([struct.pack('B',170) for _ in range(7)])
        sfd = b''.join([struct.pack('B',171)])
        eth_header = struct.pack('!6s6s2s',dst_mac, src_mac, ether_type)
        data = b''.join([struct.pack('B', random.randint(0, 255)) for _ in range(random.randint(46,max_packet_size))])
        fcs = FCS(data)
        
        packet = preamble + sfd + eth_header + data + fcs
        file.write(packet.hex() + '\n')
    file.close()