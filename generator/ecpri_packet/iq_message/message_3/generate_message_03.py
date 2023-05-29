from ..message_0to2.pc_id_generator import generate_pc_id
from ..message_0to2.seq_id_generator import generate_seq_id
from ....data.data_generator import generate_data_fixed_length
from configuration.config import config_message_00
def generate_message_03(payload_size,bytes):
    pc,seq = config_message_00()
    
    #adding PC ID
    pc_id = generate_pc_id(pc)
    bytes +=4

    #adding SEQ ID
    seq_id = generate_seq_id(seq)
    bytes +=4

    #data generation
    data,data_size = generate_data_fixed_length(int.from_bytes(payload_size, byteorder='big') - 8 , 34)
    bytes += data_size
    message = pc_id+seq_id+data
    return message,bytes