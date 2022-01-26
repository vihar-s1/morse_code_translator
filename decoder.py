from base import MORSE_CODE_DICT
import re
import encoder

def decode(encoded_string : str | None):
    encoded_string = encoded_string.strip() + " "

    if encoded_string is None or encoded_string == "":
        return None

    message = ""
    encode = ""

    for letter in encoded_string:
        if letter == '.' or letter == '-':
            encode += letter
            i = 0
        elif  letter == ' ':
            i += 1
            if i == 1:
                message += list(MORSE_CODE_DICT.keys())[ list(MORSE_CODE_DICT.values()).index(encode) ]
                encode = ""
            elif i == 2:
                message += " "
        else:
            message += letter
    
    return message
