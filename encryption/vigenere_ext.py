from .utils import get_int_representation_of

import random
import string


DEFAULT_KEY = ''.join(random.choices(string.ascii_uppercase, k = 10))

class VigenereExt:
    '''
    Implementasi Extended Vigenere Cipher.

    Cara Penggunaan
    ---------------

        from vigenere_ext import VigenereExt

        plaintext = 'hello world'

        # key harus karakter alfabet
        key = 'SOMESECRETKEYLOL'

        # enkripsi
        encrypted = VigenereExt.encrypt(plaintext, key)

        # dekripsi
        decrypted = VigenereExt.decrypt(encrypted, key)
    '''

    @staticmethod
    def encrypt(plainbytes, key = DEFAULT_KEY):
        if not key:
            raise Exception('key tidak boleh kosong')

        key_int_repr = get_int_representation_of(key)
        key_index = 0

        cipherbytes = []
        for b in plainbytes:
            cipherbytes.append((b + key_int_repr[key_index]) % 256)
            key_index = (key_index + 1) % len(key_int_repr)

        return cipherbytes
