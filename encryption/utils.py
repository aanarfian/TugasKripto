import unittest


def get_int_representation_of(text):
    uppercased = text.upper()

    int_repr = []
    for ch in uppercased:
        if not ch.isalpha():
            return None
        int_repr.append(ord(ch) - 65)

    return int_repr


class UtilsTest(unittest.TestCase):

    def test_int_representation(self):
        cases = [
            ('ABC', [0, 1, 2]),
            ('abc', [0, 1, 2]),
            ('zyx', [25, 24, 23]),
            ('ab!', None),
        ]

        for c in cases:
            expected = c[1]
            self.assertEqual(
                get_int_representation_of(c[0]),
                expected)


if __name__ == '__main__':
    unittest.main()
