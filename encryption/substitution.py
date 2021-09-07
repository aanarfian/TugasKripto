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

def decrypt_subsitution(encrypt, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    uppercased = encrypt.upper()
    decryption = ""

    for c in uppercased :
        x = re.search(c, key)
        if x:
            new_character = alphabet[x.start()]
            decryption += new_character
        else:
            decryption += c

    return decryption

# print(decrypt_subsitution("KPAKPA", "KLCODFMWSRPUENXQZITYAVJGHB"))