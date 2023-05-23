import configparser
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

    src_mac = bytes.fromhex(src_mac)
    dst_mac = bytes.fromhex(dst_mac)
    ether_type = bytes.fromhex(ether_type)
    
    stream_duration_ms=int(stream_duration_ms,10)
    ifgs = int(ifgs,16)
    max_packet_size = int(max_packet_size,10)
    burst_size = int(burst_size,10)
    burst_periodicity_us = int(burst_periodicity_us,10)

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



    protocol_version = config['PACKET_CONFIG']['PROTOCOL_VERSION'].split('x')[1]
    concatenation_indicator = config['PACKET_CONFIG']['CONCATENATION_INDICATOR'].split('x')[1]
    message_type = config['PACKET_CONFIG']['MESSAGE_TYPE'].split('x')[1]
    payload_size = config['PACKET_CONFIG']['PAYLOAD_SIZE'].split('x')[1]


    message_type = bytes.fromhex(message_type)
    payload_size = bytes.fromhex(payload_size)

    return [
            stream_duration_us \
            ,ifgs \
            ,src_mac \
            ,dst_mac \
            ,ether_type \
            ,payload_type \
            ,max_packet_size \
            ,min_packet_size\
            ,burst_size \
            ,burst_periodicity_us \
            ,protocol_version \
            ,concatenation_indicator \
            ,message_type \
            ,payload_size]

    

# configuration_ecpri()