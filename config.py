import configparser

def configuration() :
    config = configparser.ConfigParser()
    config.read('config.ini')

    stream_duration_ms=config['PACKET_CONFIG']['STREAM_DURATION_MS']
    ifgs = config['PACKET_CONFIG']['IFGs'].split('x')[1]
    src_mac = config['PACKET_CONFIG']['SOURCE_ADDRESS'].split('x')[1]
    dst_mac = config['PACKET_CONFIG']['DESTINATION_ADDRESS'].split('x')[1]
    ether_type = config['PACKET_CONFIG']['ETHER_TYPE'].split('x')[1]
    payload_type = config['PACKET_CONFIG']['PAYLOAD_TYPE']
    max_packet_size = int(config['PACKET_CONFIG']['MAX_PACKET_SIZE'],10)
    burst_size = config['PACKET_CONFIG']['BURST_SIZE']
    burst_periodicity_us = config['PACKET_CONFIG']['BURST_PERIODICITY_US']

    src_mac = bytes.fromhex(src_mac)
    dst_mac = bytes.fromhex(dst_mac)
    ether_type = bytes.fromhex(ether_type)
    
    ifgs = int(ifgs,16)
    burst_size = int(burst_size,10)
    

    return {'STREAM_DURATION_MS' : stream_duration_ms \
            ,'IFGs' : ifgs \
            , 'SOURCE_ADDRESS' : src_mac \
            , 'DESTINATION_ADDRESS' : dst_mac \
            , 'ETHER_TYPE' : ether_type \
            , 'PAYLOAD_TYPE' :payload_type \
            , 'MAX_PACKET_SIZE': max_packet_size \
            , 'BURST_SIZE' : burst_size \
            , 'BURST_PERIODICITY_US' : burst_periodicity_us}