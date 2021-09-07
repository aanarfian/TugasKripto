from ..vigenere_ext import VigenereExt

import unittest


class VigenereExtTest(unittest.TestCase):

    def test_encrypt(self):
        cases = [
            # (plainbytes, key, cipherbytes)
            ([65, 63, 66, 67, 70], 'EF', [69, 68, 70, 72, 74]),
            ([253, 254, 255], 'CYPHER', [255, 22, 14]),
        ]

        for c in cases:
            expected = c[2]
            get = VigenereExt.encrypt(c[0], c[1])
            self.assertEqual(expected, get)


    def test_decrypt(self):
        cases = [
            # (cipherbytes, key, plainbytes)
            ([69, 68, 70, 72, 74], 'EF', [65, 63, 66, 67, 70]),
            ([255, 22, 14], 'CYPHER', [253, 254, 255]),
            ([0, 1, 2, 3], 'B', [255, 0, 1, 2]),
        ]

        for c in cases:
            expected = c[2]
            get = VigenereExt.decrypt(c[0], c[1])
            self.assertEqual(expected, get)
