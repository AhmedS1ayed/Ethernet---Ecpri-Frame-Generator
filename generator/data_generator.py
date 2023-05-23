import struct
import random

def generate_data(min_data_size,max_data_size) :
    data_size = random.randint(min_data_size,max_data_size)
    data = b''.join([struct.pack('B', random.randint(0, 255)) for _ in range(data_size)])
    return data,data_size