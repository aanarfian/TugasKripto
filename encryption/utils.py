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
