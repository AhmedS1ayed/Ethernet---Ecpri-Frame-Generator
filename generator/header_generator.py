import struct
def generate_header(dst_mac,src_mac,ether_type) :
    eth_header = struct.pack('!6s6s2s',dst_mac, src_mac, ether_type)
    return eth_header