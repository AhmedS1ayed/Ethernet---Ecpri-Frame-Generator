import crcmod

def FCS(data_frame) :
    fcs_func = crcmod.predefined.Crc('crc-16')
    fcs_val = fcs_func.new(data_frame).digest()

    return fcs_val