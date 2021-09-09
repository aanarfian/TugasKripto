from typing import Text


def genereteKeyGrid(key):
    keyGrid = [[0 for x in range(5)] for y in range(5)]
    dicty = [0]*26
    for i in range(len(key)):
        if key[i] != "J":
            dicty[ord(key[i]) - 65] = 2

    dicty[ord("J") - 65] = 1
    i, j = 0, 0

    for k in range(len(key)):
        if dicty[ord(key[k]) - 65] == 2:
            dicty[ord(key[k]) - 65] -=1
            keyGrid[i][j] = key[k]
            j += 1
            if j  == 5:
                i += 1
                j = 0

    for k in range(26):
        if dicty[k] == 0:
            keyGrid[i][j] = chr(k + 65)
            j += 1
            if j == 5:
                i += 1
                j = 0

    return keyGrid

def search(keyGrid, a, b, arr):
    if a == 'j':
        a = 'i'
    elif b == 'j':
        b = 'i'
    
    for i in range(5):
        for j in range(5):
            if keyGrid[i][j] == a:
                arr[0] = i
                arr[1] = j
            elif keyGrid[i][j] == b:
                arr[2] = i
                arr[3] = j

def prepare(text, textlen):
    plaintext = list(text)
    
    if textlen % 2 != 0:
        plaintext.append('Z')
        # plaintext[textlen] = '\0'

    prepared = ''.join(plaintext)

    ps = len(text)
    
    return ps, prepared

def encrypt(text, keyGrid, textlen):
    plaintext = list(text)
    a = [0 for x in range(4)]
    for i in range(0, textlen, 2):
        search(keyGrid, plaintext[i], plaintext[i+1], a)

        if a[0] == a[2]:
            plaintext[i] = keyGrid[a[0]][(a[1]+1)%5]
            plaintext[i+1] = keyGrid[a[0]][(a[3]+1)%5]
        elif a[1] == a[3]:
            plaintext[i] = keyGrid[(a[0]+1)%5][a[1]]
            plaintext[i+1] = keyGrid[(a[2]+1)%5][a[1]]
        else:
            plaintext[i] = keyGrid[a[0]][a[3]]
            plaintext[i+1] = keyGrid[a[2]][a[1]]
    
    ciphertext = ''.join(plaintext)

    return ciphertext

def decrypt(text, keyGrid, textlen):
    plaintext = list(text)
    a = [0 for x in range(4)]
    for i in range(0, textlen, 2):
        search(keyGrid, plaintext[i], plaintext[i+1], a)

        if a[0] == a[2]:
            plaintext[i] = keyGrid[a[0]][(a[1]-1)%5]
            plaintext[i+1] = keyGrid[a[0]][(a[3]-1)%5]
        elif a[1] == a[3]:
            plaintext[i] = keyGrid[(a[0]-1)%5][a[1]]
            plaintext[i+1] = keyGrid[(a[2]-1)%5][a[1]]
        else:
            plaintext[i] = keyGrid[a[0]][a[3]]
            plaintext[i+1] = keyGrid[a[2]][a[1]]
    
    ciphertext = ''.join(plaintext)

    return ciphertext

def encrypt_playfair(plaintext, key):
    textlen = len(plaintext)

    keyGrid = genereteKeyGrid(key)

    textlen, plaintext = prepare(plaintext, textlen)

    ciphertext = encrypt(plaintext, keyGrid, textlen)

    return ciphertext

def decrypt_playfair(plaintext, key):
    textlen = len(plaintext)

    keyGrid = genereteKeyGrid(key)

    textlen, plaintext = prepare(plaintext, textlen)

    ciphertext = decrypt(plaintext, keyGrid, textlen)

    return ciphertext

# print(playfair("INSTRUMENTS", "MONARCHY"))
print(decrypt_playfair("GATLMZCLRQ","MONARCHY"))



