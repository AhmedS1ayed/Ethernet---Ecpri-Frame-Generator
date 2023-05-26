from .pc_id_generator import generate_pc_id
from .seq_id_generator import generate_seq_id
from ....data_generator import generate_data_fixed_length
from config import config_message_00
def generate_message_00(payload_size,bytes):
    pc,seq = config_message_00()
    
    #adding PC ID
    pc_id = generate_pc_id(pc)
    bytes +=2

    #adding SEQ ID
    seq_id = generate_seq_id(seq)
    bytes +=2

    #data generation
    data,data_size = generate_data_fixed_length(int.from_bytes(payload_size, byteorder='big') - 4 , 38)
    bytes += data_size
    message = pc_id+seq_id+data
    return message,bytes