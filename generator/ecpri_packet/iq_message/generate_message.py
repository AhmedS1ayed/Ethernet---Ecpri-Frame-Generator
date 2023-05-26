from .message_0.generate_message_00 import generate_message_00
def generate_message(message_type,payload_size,bytes):
    if(message_type.hex() == '00'):
        return generate_message_00(payload_size,bytes)
    if(message_type.hex() == '01'):
        return generate_message_00(payload_size,bytes)
    if(message_type.hex() == '10'):
        return generate_message_00(payload_size,bytes)
