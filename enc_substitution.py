import re

def encrypt_subsitution(text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    uppercased = text.upper()
    encryption = ""

    for c in uppercased :
        x = re.search(c, alphabet)
        if x :
            new_character = key[x.start()]
            encryption += new_character
        else:
            encryption += c

    return encryption