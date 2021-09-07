from ..utils import get_int_representation_of, get_text_from

import unittest


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
