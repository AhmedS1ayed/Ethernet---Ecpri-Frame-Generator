import crcmod

def generate_crc(data_frame) :
    crc_func = crcmod.predefined.Crc('crc-16')
    crc_val = crc_func.new(data_frame).digest()
    return crc_val