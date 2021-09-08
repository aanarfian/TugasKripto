def encrypt_vigenere(text, key):
    encryptedText = ""
    if len(text) != len(key):
        for i in range(len(text) - len(key)):
            key += key[i % len(key)]

    for i in range(len(text)):
        c = ((ord(text[i]) + ord(key[i])) % 26) + ord('A')
        encryptedText += chr(c)
    
    return encryptedText

def decrypt_vigenere(text, key):
    decryptedText = ""
    if len(text) != len(key):
        for i in range(len(text) - len(key)):
            key += key[i % len(key)]

    for i in range(len(text)):
        c = ((ord(text[i]) - ord(key[i]) + 26) % 26) + ord('A')
        decryptedText += chr(c)
    
    return decryptedText