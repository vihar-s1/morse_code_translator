from DataSet import MORSE_CODE_DICT


def decode(encoded_string: str | None):
    '''
    Decodes the given encoded string. Only focuses on valid encoded portions.
    '''
    encoded_string = encoded_string.strip() + " "

    if encoded_string is None or encoded_string == "":
        return None

    message = ""
    encoding = ""

    for letter in encoded_string:
        if letter == '.' or letter == '-':
            encoding += letter
            i = 0
        elif letter == ' ':
            i += 1
            if i == 1:
                message += list(MORSE_CODE_DICT.keys()
                                )[list(MORSE_CODE_DICT.values()).index(encoding)]
                encoding = ""
            elif i == 2:
                message += " "
        else:
            message += letter

    return message


def encode(message: str | None):
    '''
    Encodes given string in morse code. Only converts characters present in the DataSet.
    '''
    message = message.strip().upper()
    if message is None or message == "":
        return None

    encoded_string = ""
    for letter in message:
        encode = MORSE_CODE_DICT.get(key=letter, default=letter) + " "
        encoded_string += encode
    return encoded_string
