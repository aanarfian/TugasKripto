from utils import get_int_representation_of, get_text_from

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
        ENCRYPT_FUNC = lambda x: (a * x + b) % 26

        int_repr = get_int_representation_of(plaintext)
        if int_repr == None:
            raise Exception('tidak support karakter selain alfabet')
    
        encrypted_int_repr = [ENCRYPT_FUNC(x) for x in int_repr]
        return get_text_from(encrypted_int_repr)


    @staticmethod
    def decrypt(ciphertext, a = 5, b = 3):
        a_invers = [i for i in range(26) if (a * i) % 26 == 1][0]
        DECRYPT_FUNC = lambda y: (a_invers * (y - b)) % 26

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
        cases = [
            # (text, key_a, key_b)
            ('helloworld', 3, 2),
            ('affine', 5, 1),
            ('laksjfdpi', 9, 5),
            ('AAA', 11, 17),
        ]

        for c in cases:
            a = c[1]
            b = c[2]
            encrypted = Affine.encrypt(c[0], a, b)
            decrypted = Affine.decrypt(encrypted, a, b)
            self.assertEqual(c[0].upper(), decrypted)


if __name__ == '__main__':
    unittest.main()
