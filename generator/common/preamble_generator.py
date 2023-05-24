import struct
def generate_preamble():
    return b''.join([struct.pack('B',170) for _ in range(7)])