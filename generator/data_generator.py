import struct
import random

def generate_data(min_data_size,max_data_size) :
    data_size = random.randint(min_data_size,max_data_size)
    data = b''.join([struct.pack('B', random.randint(0, 255)) for _ in range(426)])
    return data,data_size

def generate_data_fixed_length(payload_size) :
    size = int.from_bytes(payload_size, byteorder='big')
    data = b''.join([struct.pack('B', random.randint(0, 255)) for _ in range(size)])
    #make the rest zeros
    rem = 46 - size
    data += b''.join([struct.pack('B', 0) for _ in range(rem)])
    return data,46