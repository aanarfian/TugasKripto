from .utils import get_int_representation_of, get_text_from

import math
import unittest


class Affine:
    '''
    Implementasi algoritma Affine Cipher.

    Cara Penggunaan
    ---------------
     1. Enkripsi

            from affine import Affine

            plaintext = 'hello world'

            a = 5
            b = 3
            ciphertext = Affine.encrypt(plaintext, a, b)


     2. Dekripsi

            from affine import Affine

            ciphertext = 'blah blah blah'

            a = 5
            b = 3
            plaintext = Affine.decrypt(ciphertext, a, b)
    '''

    @staticmethod
    def encrypt(plaintext, a = 5, b = 3):
        if math.gcd(a, 26) > 1:
            raise Exception('key a harus berupa bilangan yang coprime dengan 26')

        ENCRYPT_FUNC = lambda x: (a * x + b) % 26

        int_repr = get_int_representation_of(plaintext)
        if int_repr == None:
            raise Exception('tidak support karakter selain alfabet')

        encrypted_int_repr = [ENCRYPT_FUNC(x) for x in int_repr]
        return get_text_from(encrypted_int_repr)


    @staticmethod
    def decrypt(ciphertext, a = 5, b = 3):
        if math.gcd(a, 26) > 1:
            raise Exception('key a harus berupa bilangan yang coprime dengan 26')

        a_invers = [i for i in range(26) if (a * i) % 26 == 1][0]
        DECRYPT_FUNC = lambda y: (a_invers * (y - b)) % 26

        int_repr = get_int_representation_of(ciphertext)
        if int_repr == None:
            raise Exception('invalid cipher text')

        decrypted_int_repr = [DECRYPT_FUNC(y) for y in int_repr]
        return get_text_from(decrypted_int_repr)
