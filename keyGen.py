import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'


def keyBlock():
    chars = []
    for i in range(2):
        chars.append(random.choice(DIGITS))
    for i in range(3):
        chars.append(random.choice(LETTERS))
    random.shuffle(chars)

    block = ''
    for c in chars:
        block += c
    return block


def keyGeneration():
    key = f'{keyBlock()}-{keyBlock()}-{keyBlock()}'
    return key
