import re

def decrypt_subsitution(encrypt, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypt.upper()
    decryption = ""

    for c in encrypt :
        x = re.search(c, key)
        if x:
            new_character = alphabet[x.start()]
            decryption += new_character
        else:
            decryption += c

    return decryption

print(decrypt_subsitution("KPAKPA", "KLCODFMWSRPUENXQZITYAVJGHB"))