import unittest


def get_int_representation_of(text):
    uppercased = text.upper()

    int_repr = []
    for ch in uppercased:
        if not ch.isalpha():
            return None
        int_repr.append(ord(ch) - 65)

    return int_repr

def get_text_from(int_repr):
    text = []
    for x in int_repr:
        if not 0 <= x <= 25:
            return None
        text.append(chr(x + 65))

    return ''.join(text)    


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

    def test_int_representation_to_text(self):
        cases = [
            ([0, 1, 2], 'ABC'),
            ([23, 24, 25], 'XYZ'),
            ([26, 27, 28], None),
        ]

        for c in cases:
            expected = c[1]
            self.assertEqual(
                get_text_from(c[0]),
                expected)


if __name__ == '__main__':
    unittest.main()
