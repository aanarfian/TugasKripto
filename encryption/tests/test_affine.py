from ..affine import Affine

import unittest


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

        invalid_cases = [
            # (text, a, b)
            ('123', 3, 5),  # invalid input
            ('abc', 13, 2), # key a bukan coprime dari 26
        ]

        for c in invalid_cases:
            self.assertRaises(Exception, Affine.encrypt, c[0], c[1], c[2])


    def test_decrypt(self):
        cases = [
            ('NKTAUV', 'CRYPTO'),
            ('MXGGVJVKGS', 'HELLOWORLD'),
        ]

        for c in cases:
            expected = c[1]
            plaintext = Affine.decrypt(c[0])
            self.assertEqual(expected, plaintext)

        invalid_cases = [
            # (text, a, b)
            ('123', 3, 5),  # invalid input
            ('abc', 13, 2), # key a bukan coprime dari 26
        ]

        for c in invalid_cases:
            self.assertRaises(Exception, Affine.decrypt, c[0], c[1], c[2])


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
