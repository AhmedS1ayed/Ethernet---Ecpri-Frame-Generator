import struct
def generate_ecpri_header(protocol_version,concatenation_indicator,message_type,payload_size) :
    ecpri_header = struct.pack('!2s2s4s',protocol_version+concatenation_indicator , message_type,payload_size)
    return ecpri_header