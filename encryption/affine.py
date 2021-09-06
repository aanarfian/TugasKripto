from utils import get_int_representation_of, get_text_from

import unittest


ENCRYPTION_KEY = (5, 3)

ENCRYPT_FUNC = lambda x: (ENCRYPTION_KEY[0] * x + ENCRYPTION_KEY[1]) % 26
# TODO: Buat logika untuk mendapatkan invers dari A.
#       Pada fungsi dekripsi di bawah ini, invers dari
#       A diberikan secara manual (hardcoded). Sehingga
#       apabila encryption key berubah, maka fungsi ini
#       harus diubah kembali
DECRYPT_FUNC = lambda y: (21 * (y - ENCRYPTION_KEY[1])) % 26

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

            plaintext = Affine.decrypt(ciphertext)
    '''

    @staticmethod
    def encrypt(plaintext, a = 5, b = 3):
        ENCRYPT_FUNC = lambda x: (a * x + b) % 26

        int_repr = get_int_representation_of(plaintext)
        if int_repr == None:
            raise Exception('tidak support karakter selain alfabet')
    
        encrypted_int_repr = [ENCRYPT_FUNC(x) for x in int_repr]
        return get_text_from(encrypted_int_repr)


    @staticmethod
    def decrypt(ciphertext):
        int_repr = get_int_representation_of(ciphertext)
        if int_repr == None:
            raise Exception('invalid cipher text')

        decrypted_int_repr = [DECRYPT_FUNC(y) for y in int_repr]
        return get_text_from(decrypted_int_repr)


class AffineTest(unittest.TestCase):

    def test_encrypt(self):
        cases = [
            ('CRYPTO', 'NKTAUV'),
            ('crypto', 'NKTAUV'),
        ]

        for c in cases:
            expected = c[1]
            ciphertext = Affine.encrypt(c[0])
            self.assertEqual(expected, ciphertext)

        # invalid test case
        invalid_plaintext = '123!@#'
        self.assertRaises(Exception, Affine.encrypt, invalid_plaintext)


    def test_decrypt(self):
        cases = [
            ('NKTAUV', 'CRYPTO'),
            ('MXGGVJVKGS', 'HELLOWORLD'),
        ]

        for c in cases:
            expected = c[1]
            plaintext = Affine.decrypt(c[0])
            self.assertEqual(expected, plaintext)

        # invalid test case
        invalid_ciphertext = '@12345'
        self.assertRaises(Exception, Affine.decrypt, invalid_ciphertext)


    def test_encrypt_decrypt(self):
        texts = ['helloworld', 'affine', 'laksjfdpi', 'AAA']

        for text in texts:
            encrypted = Affine.encrypt(text)
            decrypted = Affine.decrypt(encrypted)
            self.assertEqual(text.upper(), decrypted)


if __name__ == '__main__':
    unittest.main()
