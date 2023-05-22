import struct
import random
from config import configuration
from FCS import FCS

configs = configuration()

burst_size = configs['BURST_SIZE']
ifgs = configs['IFGs']
src_mac = configs['SOURCE_ADDRESS']
dst_mac = configs['DESTINATION_ADDRESS']
ether_type = configs['ETHER_TYPE']
max_packet_size = configs['MAX_PACKET_SIZE']
min_packet_size = 72



max_data_size = max_packet_size - 26
min_data_size = min_packet_size - 26 #46-byte

with open('packets.txt', 'w') as file:
    for i in range(burst_size):
        preamble = b''.join([struct.pack('B',170) for _ in range(7)])
        sop = b''.join([struct.pack('B',171)])
        eth_header = struct.pack('!6s6s2s',dst_mac, src_mac, ether_type)

        data_size = random.randint(min_data_size,max_data_size)
        data = b''.join([struct.pack('B', random.randint(0, 255)) for _ in range(data_size)])
        fcs = FCS(data)
        
        packet = preamble + sop + eth_header + data + fcs
        file.write(packet.hex() + '\n')


        no_ifgs = random.randrange(4, 20 , 4)
        ifg_cycle = b''.join([struct.pack('B',ifgs) for _ in range(no_ifgs)])
        file.write(ifg_cycle.hex() + '\n')
        
    file.close()



#64-byte : is the minimum size of ethernet-frame excluding preamble and sop
#8-byte : preamble + sop 
#min-size-of-whole-packet : 64byte(ethernet-frame) + 8byte(preamble&sop) = 72-byte
#26-byte = 7-preamble + 1-sop + 6-dst + 6-src + 2-type + 4-fcs      <========
#min-size-of-data : 64+8
#max-size-of-data : max-packet-size - 26