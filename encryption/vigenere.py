alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def evaluate_key(text, key):
    if len(text) != len(key):
        for i in range(len(text) - len(key)):
            key += key[i % len(key)]
    return key


def encrypt_vigenere(text, key):
    key = evaluate_key(text, key)
    encryptedText = ""

    for i in range(len(text)):
        c = (letter_to_index[text[i]] + letter_to_index[key[i]]) % 26
        encryptedText += index_to_letter[c]
    
    return encryptedText

def decrypt_vigenere(text, key):
    key = evaluate_key(text, key)
    decryptedText = ""

    for i in range(len(text)):
        d = (letter_to_index[text[i]] - letter_to_index[key[i]]) % 26
        decryptedText += index_to_letter[d]
    
    return decryptedText