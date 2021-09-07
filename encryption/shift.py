def decrypt_shitt(encrypted_text, shift):
    text = ""
    for c in encrypted_text:
        if c.isupper():
            c_index = ord(c) - ord("A")
            index_baru = (c_index - shift) % 26
            unicode_baru = index_baru + ord("A")
            karakter_baru = chr(unicode_baru)
            text += karakter_baru

        else:
            # since karakter is not uppercase, leave it as it is
            text += c

    return text

def encrypt_shitt(text, shift):
    encryption = ""
    for c in text:
        if c.isupper():
            c_index = ord(c) - ord("A")
            index_baru = (c_index + shift) % 26
            unicode_baru = index_baru + ord("A")
            karakter_baru = chr(unicode_baru)
            encryption = encryption + karakter_baru

        else:
            encryption += c
            
    return encryption



