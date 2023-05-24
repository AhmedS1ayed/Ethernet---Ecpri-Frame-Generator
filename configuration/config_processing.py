def fix_config(src_mac,dst_mac,ether_type,stream_duration_ms,ifgs,max_packet_size,burst_size,burst_periodicity_us):
    src_mac = bytes.fromhex(src_mac)
    dst_mac = bytes.fromhex(dst_mac)
    ether_type = bytes.fromhex(ether_type)
    
    stream_duration_ms=int(stream_duration_ms,10)
    ifgs = int(ifgs,16)
    max_packet_size = int(max_packet_size,10)
    burst_size = int(burst_size,10)
    burst_periodicity_us = int(burst_periodicity_us,10)

    return [src_mac,dst_mac,ether_type,stream_duration_ms,ifgs,max_packet_size,burst_size,burst_periodicity_us]

def fix_config_ecpri(protocol_version,concatenation_indicator,message_type,payload_size):
    protocol_version += "0"
    concatenation_indicator = "0"+ concatenation_indicator

    protocol_version = bytes.fromhex(protocol_version)
    concatenation_indicator = bytes.fromhex(concatenation_indicator)
    message_type = bytes.fromhex(message_type)
    payload_size = bytes.fromhex(payload_size)

    return [protocol_version,concatenation_indicator,message_type,payload_size]