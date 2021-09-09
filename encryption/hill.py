import numpy as np
from egcd import egcd

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def key_to_matrix(key):
    return np.matrix(key)

def encrypt_hill(text, key):
    key = key_to_matrix(key)
    encrypted_text = ""
    text_index = []

    for i in text:
        text_index.append(letter_to_index[i])

    split_ptext = [text_index[i:i+int(key.shape[0])] for i in range(0, len(text_index), int(key.shape[0]))]

    for X in split_ptext:
        X = np.transpose(np.asarray(X))[:, np.newaxis]

        while X.shape[0] != key.shape[0]:
            X = np.append(X, letter_to_index['X'])

        numbers = np.dot(key, X) % len(alphabet)
        n = numbers.shape[0]

        for index in range(n):
            number = int(numbers[index, 0])
            encrypted_text += index_to_letter[number]

    return encrypted_text

def inverse_matrix_modm(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_inv_mod = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus)

    return matrix_inv_mod

def decrypt_hill(text, key):
    key = key_to_matrix(key)
    key = inverse_matrix_modm(key, len(alphabet))

    decrypted_text = ""
    text_index = []

    for i in text:
        text_index.append(letter_to_index[i])

    split_ctext = [text_index[i:i+int(key.shape[0])] for i in range(0, len(text_index), int(key.shape[0]))]   

    for X in split_ctext:
        X = np.transpose(np.asarray(X))[:, np.newaxis]
        numbers = np.dot(key, X) % len(alphabet)
        n = numbers.shape[0]

        for index in range(n):
            number = int(numbers[index, 0])
            decrypted_text += index_to_letter[number]

    return decrypted_text