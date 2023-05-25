import struct
import random
import math
from config import configuration,configuration_ecpri
from ..data_generator import generate_data
from ..common.crc_generator import generate_crc
from ..common.header_generator import generate_header
from ..common.ifg_generator import generate_ifg , generate_break_ifg
from ..common.preamble_generator import generate_preamble
from ..common.sop_generator import generate_sop
from config import get_fname

def generate_eth(bytes_due_stream,bytes_per_period,burst_size,dst_mac,src_mac,ether_type,min_data_size,max_data_size,ifgs):
    bytes = 0
    bytes_due_period = 0
    with open(get_fname(), 'w') as file:
        while bytes < bytes_due_stream:
            bytes_due_period +=  bytes_per_period
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
                    break

                

                #construct the packet
                packet = preamble + sop + eth_header + data + crc
                file.write(packet.hex() + '\n')

                #ifg generation
                ifg,no_ifgs = generate_ifg(ifgs)
                file.write(ifg.hex() + '\n')
                bytes += no_ifgs
                print('bytes : ' + str(bytes) + ' bytesDP :' + str(bytes_due_period))
            #if the burst is over before going to next burst fill the rest of the burst with ifgs
            while(bytes < bytes_due_period):
                no_ifgs = bytes_due_period - bytes  
                ifg,no_ifgs = generate_break_ifg(ifgs,no_ifgs)
                file.write(ifg.hex() + '\n')
                bytes += no_ifgs
                print('bytes : ' + str(bytes) + ' bytesDP :' + str(bytes_due_period))

        file.close()