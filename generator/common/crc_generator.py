import binascii

def generate_crc(data_frame) :
    crc_val = binascii.crc32(data_frame)
    crc = crc_val.to_bytes(4, byteorder='big')
    return crc