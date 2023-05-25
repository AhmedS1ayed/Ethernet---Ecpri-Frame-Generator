import binascii

def generate_crc(data_frame) :
    crc_val = binascii.crc32(data_frame)
    crc_val = crc_val.to_bytes(4, byteorder='big')
    print('crc val :' , crc_val)
    return crc_val