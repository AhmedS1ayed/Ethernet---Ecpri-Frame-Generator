import configparser
from config_processing import fix_config,fix_config_ecpri
config = configparser.ConfigParser()
config.read('config.ini')

def configuration() :
    global config
    stream_duration_ms = config['PACKET_CONFIG']['STREAM_DURATION_MS']
    ifgs = config['PACKET_CONFIG']['IFGs'].split('x')[1]
    src_mac = config['PACKET_CONFIG']['SOURCE_ADDRESS'].split('x')[1]
    dst_mac = config['PACKET_CONFIG']['DESTINATION_ADDRESS'].split('x')[1]
    ether_type = config['PACKET_CONFIG']['ETHER_TYPE'].split('x')[1]
    payload_type = config['PACKET_CONFIG']['PAYLOAD_TYPE']
    max_packet_size = config['PACKET_CONFIG']['MAX_PACKET_SIZE']
    min_packet_size = 72
    burst_size = config['PACKET_CONFIG']['BURST_SIZE']
    burst_periodicity_us = config['PACKET_CONFIG']['BURST_PERIODICITY_US']

    src_mac,dst_mac,ether_type,stream_duration_ms,ifgs,max_packet_size,burst_size,burst_periodicity_us = fix_config(src_mac,dst_mac,ether_type,stream_duration_ms,ifgs,max_packet_size,burst_size,burst_periodicity_us)

    return [stream_duration_ms*1000 \
            ,ifgs \
            ,src_mac \
            ,dst_mac \
            ,ether_type \
            ,payload_type \
            ,max_packet_size \
            ,min_packet_size\
            ,burst_size \
            ,burst_periodicity_us]



def configuration_ecpri() :
    global config
    protocol_version = config['PACKET_CONFIG']['PROTOCOL_VERSION']
    concatenation_indicator = config['PACKET_CONFIG']['CONCATENATION_INDICATOR']
    message_type = config['PACKET_CONFIG']['MESSAGE_TYPE'].split('x')[1]
    payload_size = config['PACKET_CONFIG']['PAYLOAD_SIZE'].split('x')[1]

    protocol_version += "0"
    concatenation_indicator = "0"+ concatenation_indicator

    protocol_version,concatenation_indicator,message_type,payload_size = fix_config_ecpri(protocol_version,concatenation_indicator,message_type,payload_size)
    return [protocol_version \
            ,concatenation_indicator \
            ,message_type \
            ,payload_size]

    

# configuration_ecpri()