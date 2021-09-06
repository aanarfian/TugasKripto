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

