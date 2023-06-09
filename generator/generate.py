import struct
import random
import math
from configuration.config import configuration,configuration_ecpri
from generator.ethernet_packet.generate_ethernet import generate_eth
from generator.ecpri_packet.generate_ecpri import generate__ecpri
from generator.IEEE_802_3.generate_IEEE_802_3 import generate_IEEE_802_3

def generate(type) :
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
    #note : 12 is for ifg bytes
    bytes_per_us =  (max_packet_size + 12) * burst_size / burst_periodicity_us
    bytes_per_period = math.ceil(bytes_per_us * burst_periodicity_us)
    bytes_due_stream = math.ceil(bytes_per_us * stream_duration_us)

    #calculations of data size
    max_data_size = max_packet_size - 26
    min_data_size = min_packet_size - 26 #46-byte

    if(type == 'ethernet'):
        generate_eth(bytes_due_stream,bytes_per_period,burst_size,dst_mac,src_mac,ether_type,min_data_size,max_data_size,ifgs)


    elif(type == 'ecpri'):
        protocol_version \
        ,concatenation_indicator \
        ,message_type \
        ,payload_size = configuration_ecpri()
        generate__ecpri(bytes_due_stream,bytes_per_period,burst_size,dst_mac,src_mac,ether_type,ifgs,protocol_version,concatenation_indicator,message_type,payload_size)

    elif(type =='IEEE 802.3'):
        generate_IEEE_802_3(bytes_due_stream,bytes_per_period,burst_size,dst_mac,src_mac,ether_type,min_data_size,max_data_size,ifgs)
        
#64-byte : is the minimum size of ethernet-frame excluding preamble and sop
#8-byte : preamble + sop 
#min-size-of-whole-packet : 64byte(ethernet-frame) + 8byte(preamble&sop) = 72-byte
#26-byte = 7-preamble + 1-sop + 6-dst + 6-src + 2-type + 4-fcs      <========
#min-size-of-data : 64 + 8 - 26
#max-size-of-data : max-packet-size - 26

###################################################################################### packets and time

#max-packet-size * burst-size / burst-periodicity = bytes per microsecond