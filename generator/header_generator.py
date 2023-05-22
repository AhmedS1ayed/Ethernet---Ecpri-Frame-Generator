import struct
def generate_header(dst_mac,src_mac,ether_type) :
    preamble = b''.join([struct.pack('B',170) for _ in range(7)])
    sop = b''.join([struct.pack('B',171)])
    eth_header = struct.pack('!6s6s2s',dst_mac, src_mac, ether_type)
    return eth_header