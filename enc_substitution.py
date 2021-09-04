import re

def encrypt_subsitution(text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text.upper()
    encryption = ""

    for c in text :
        if re.search(c, alphabet):
            x = re.search(c, alphabet)
            new_character = key[x.start()]
            encryption += new_character
        else:
            encryption += c

    return encryption