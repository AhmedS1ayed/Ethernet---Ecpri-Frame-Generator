from .message_0to2.generate_message_00 import generate_message_00
from .message_3.generate_message_03 import generate_message_03
def generate_message(message_type,payload_size,bytes):
    if(message_type.hex() == '00' or message_type.hex() == '01' or message_type.hex() == '02'):
        return generate_message_00(payload_size,bytes)
    elif(message_type.hex() == '03'):
        return generate_message_03(payload_size,bytes)

