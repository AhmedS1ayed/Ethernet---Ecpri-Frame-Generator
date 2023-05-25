import struct
def generate_sop():
    return b''.join([struct.pack('B',171) for _ in range(1)])