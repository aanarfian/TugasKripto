import unittest


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
        pass

    @staticmethod
    def decrypt(ciphertext):
        pass


class AffineTest(unittest.TestCase):

    def test_encrypt(self):
        pass

    def test_decrypt(self):
        pass

    def test_encrypt_decrypt(self):
        pass


if __name__ == '__main__':
    unittest.main()
