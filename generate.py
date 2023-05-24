import struct
import random
import sys
import math
from config.config import configuration,configuration_ecpri
from data_generator import generate_data,generate_data_ecpri
from crc_generator import generate_crc
from header_generator import generate_header
from ecpri_header_generator import generate_ecpri_header
from ifg_generator import generate_ifg , generate_break_ifg
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

#data rate and time to byte conversion calculations
bytes_per_us = math.floor(max_packet_size * burst_size / burst_periodicity_us)
bytes_per_period = bytes_per_us * burst_periodicity_us
bytes_due_stream = bytes_per_us * stream_duration_us

#calculations of data size
max_data_size = max_packet_size - 26
min_data_size = min_packet_size - 26 #46-byte




def generate_eth():
    bytes = 0
    with open('packets.txt', 'w') as file:
        while bytes < bytes_due_stream:
            bytes_due_period = bytes + bytes_per_period
            for i in range(burst_size):
                bytes_before_cycle = bytes

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

                #check if the frame can be sent and if it can't , send ifgs instead and make them a multiple of 4 :
                if(bytes > bytes_due_stream):
                    #replace bytes remained with ifgs
                    no_ifgs = bytes_due_stream - bytes_before_cycle

                    #generate ifgs instead of packets
                    ifg,no_ifgs = generate_break_ifg(ifgs,no_ifgs)
                    file.write(ifg.hex() + '\n')
                    
                    bytes = bytes_before_cycle + no_ifgs
                    break
                
                if(bytes > bytes_due_period):
                    #replace bytes remained with ifgs
                    no_ifgs = bytes_due_period - bytes_before_cycle  

                    #generate ifgs instead of packets
                    ifg,no_ifgs = generate_break_ifg(ifgs,no_ifgs)
                    file.write(ifg.hex() + '\n')
                    
                    bytes = bytes_before_cycle + no_ifgs
                    bytes_due_period += bytes_per_period
                    break

                # print('bytes : ' + str(bytes) + ' bytesDP :' + str(bytes_due_period))

                #construct the packet
                packet = preamble + sop + eth_header + data + crc
                file.write(packet.hex() + '\n')

                #ifg generation
                ifg,no_ifgs = generate_ifg(ifgs)
                file.write(ifg.hex() + '\n')
                bytes += no_ifgs

        file.close()

def generate_ecpri():

    protocol_version \
    ,concatenation_indicator \
    ,message_type \
    ,payload_size = configuration_ecpri()
    bytes = 0

    with open('packets.txt', 'w') as file:
        while bytes < bytes_due_stream:
            bytes_due_period = bytes + bytes_per_period
            for i in range(burst_size):
                bytes_before_cycle = bytes

                #preamble & sop generation
                preamble = generate_preamble()
                sop = generate_sop()
                bytes += 8

                #header generation
                eth_header = generate_header(dst_mac,src_mac,ether_type)
                bytes += 14

                #ecpri header generation
                ecpri_header = generate_ecpri_header(protocol_version,concatenation_indicator,message_type,payload_size)
                bytes += 4

                #data generation
                data,data_size = generate_data_ecpri(payload_size)
                bytes += data_size

                #fcs generation
                crc = generate_crc(data)
                bytes += 4

                #check if the frame can be sent and if it can't , send ifgs instead and make them a multiple of 4 :
                if(bytes > bytes_due_stream):
                    #replace bytes remained with ifgs
                    no_ifgs = bytes_due_stream - bytes_before_cycle

                    #generate ifgs instead of packets
                    ifg,no_ifgs = generate_break_ifg(ifgs,no_ifgs)
                    file.write(ifg.hex() + '\n')
                    
                    bytes = bytes_before_cycle + no_ifgs
                    break
                
                if(bytes > bytes_due_period):
                    #replace bytes remained with ifgs
                    no_ifgs = bytes_due_period - bytes_before_cycle  

                    #generate ifgs instead of packets
                    ifg,no_ifgs = generate_break_ifg(ifgs,no_ifgs)
                    file.write(ifg.hex() + '\n')
                    
                    bytes = bytes_before_cycle + no_ifgs
                    bytes_due_period += bytes_per_period
                    break

                # print('bytes : ' + str(bytes) + ' bytesDP :' + str(bytes_due_period))

                #construct the packet
                packet = preamble + sop + eth_header + ecpri_header + data + crc
                file.write(packet.hex() + '\n')

                #ifg generation
                ifg,no_ifgs = generate_ifg(ifgs)
                file.write(ifg.hex() + '\n')
                bytes += no_ifgs

        file.close()



#64-byte : is the minimum size of ethernet-frame excluding preamble and sop
#8-byte : preamble + sop 
#min-size-of-whole-packet : 64byte(ethernet-frame) + 8byte(preamble&sop) = 72-byte
#26-byte = 7-preamble + 1-sop + 6-dst + 6-src + 2-type + 4-fcs      <========
#min-size-of-data : 64 + 8 - 26
#max-size-of-data : max-packet-size - 26

###################################################################################### packets and time

#max-packet-size * burst-size / burst-periodicity = bytes per microsecond