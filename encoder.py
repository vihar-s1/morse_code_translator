from base import MORSE_CODE_DICT

def encode(message : str | None):
    message = message.strip().upper()
    if message is None or message == "":
        return None
    
    encoded_string = ""
    for letter in message:
        encode = MORSE_CODE_DICT.get( letter, letter ) + " "
        encoded_string += encode
    return encoded_string