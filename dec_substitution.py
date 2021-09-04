import re

def decrypt_subsitution(encrypt, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypt.upper()
    decryption = ""

    for c in encrypt :
        if re.search(c, key):
            x = re.search(c, key)
            new_character = alphabet[x.start()]
            decryption += new_character
        else:
            decryption += c

    return decryption

print(decrypt_subsitution("KPAKPA", "KLCODFMWSRPUENXQZITYAVJGHB"))