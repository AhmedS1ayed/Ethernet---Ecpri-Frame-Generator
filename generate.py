import struct
import random
import sys
sys.path.append("./generator")
from config import configuration,configuration_ecpri
from data_generator import generate_data
from crc_generator import generate_crc
from header_generator import generate_header
from ifg_generator import generate_ifg
from preamble_generator import generate_preamble
from sop_generator import generate_sop


stream_duration_us \
,ifgs \
,src_mac \
,dst_mac \
,ether_type \
,payload_type \
,max_packet_size \
,min_packet_size\
,burst_size \
,burst_periodicity_us = configuration()

bytes_per_us = max_packet_size * burst_size / burst_periodicity_us
bytes_per_stream = bytes_per_us * stream_duration_us
bytes = 0

#calculations of data size
max_data_size = max_packet_size - 26
min_data_size = min_packet_size - 26 #46-byte


def generate():
    global bytes
    with open('packets.txt', 'w') as file:
        while bytes < bytes_per_stream:
            for i in range(burst_size):
                #preamble & sop generation
                preamble = generate_preamble()
                sop = generate_sop()
                bytes += 8

                #header generation
                eth_header = generate_header(dst_mac,src_mac,ether_type)
                bytes += 14

                #data generation
                data,data_size = generate_data(min_data_size,max_data_size)
                bytes += data_size

                #fcs generation
                crc = generate_crc(data)
                bytes += 4

                #check if the frame can be sent
                if(bytes > bytes_per_stream):
                    break

                #construct the packet
                packet = preamble + sop + eth_header + data + crc
                file.write(packet.hex() + '\n')

                #ifg generation
                ifg,no_ifgs = generate_ifg(ifgs)
                bytes += no_ifgs
                file.write(ifg.hex() + '\n')

        file.close()

def generate_ecpri():
    with open('packets.txt', 'w') as file:
        while time < stream_duration_us :
            for i in range(burst_size):
                #calculating time to send this packet
                time += packet_periodicity
                if(time > stream_duration_us):
                    break

                #preamble & sop generation
                preamble = generate_preamble()
                sop = generate_sop()

                #header generation
                eth_header = generate_header(dst_mac,src_mac,ether_type)

                #data generation
                data = generate_data(min_data_size,max_data_size)

                #fcs generation
                crc = generate_crc(data)

                #construct the packet
                packet = preamble + sop + eth_header + data + crc
                file.write(packet.hex() + '\n')

                #ifg generation
                ifg = generate_ifg(ifgs)
                file.write(ifg.hex() + '\n')

        file.close()



#64-byte : is the minimum size of ethernet-frame excluding preamble and sop
#8-byte : preamble + sop 
#min-size-of-whole-packet : 64byte(ethernet-frame) + 8byte(preamble&sop) = 72-byte
#26-byte = 7-preamble + 1-sop + 6-dst + 6-src + 2-type + 4-fcs      <========
#min-size-of-data : 64 + 8 - 26
#max-size-of-data : max-packet-size - 26

###################################################################################### packets and time

#max-packet-size * burst-size / burst-periodicity = bytes per microsecond