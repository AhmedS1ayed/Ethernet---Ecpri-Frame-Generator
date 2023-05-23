import struct
import random
def generate_ifg(ifgs) :
    no_ifgs = random.randrange(4, 20 , 4)
    ifg_cycle = b''.join([struct.pack('B',ifgs) for _ in range(no_ifgs)])
    return ifg_cycle,no_ifgs

def generate_break_ifg(ifgs,no_ifgs) :
    ifg_cycle = b''.join([struct.pack('B',ifgs) for _ in range(no_ifgs)])
    return ifg_cycle