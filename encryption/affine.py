from utils import get_int_representation_of, get_text_from

import unittest


ENCRYPTION_KEY = (5, 3)

ENCRYPT_FUNC = lambda x: (ENCRYPTION_KEY[0] * x + ENCRYPTION_KEY[1]) % 26

class Affine:
    '''
    Implementasi algoritma Affine Cipher.

    Cara Penggunaan
    ---------------
     1. Enkripsi

            from affine import Affine

            plaintext = 'hello world'

            ciphertext = Affine.encrypt(plaintext)


     2. Dekripsi

            from affine import Affine

            ciphertext = 'blah blah blah'

            plaintext = Affine.decrypt(ciphertext)
    '''

    @staticmethod
    def encrypt(plaintext):
        int_repr = get_int_representation_of(plaintext)
        if int_repr == None:
            raise Exception('tidak support karakter selain alfabet')
    
        encrypted_int_repr = [ENCRYPT_FUNC(x) for x in int_repr]
        return get_text_from(encrypted_int_repr)


    @staticmethod
    def decrypt(ciphertext):
        pass


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
        pass

    def test_encrypt_decrypt(self):
        pass


if __name__ == '__main__':
    unittest.main()
