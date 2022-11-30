from itertools import *
import string

ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def b16_decode(enc):
    dec = ""
    for i in range(0, len(enc), 2):
        binary = "{0:04b}".format(ALPHABET.index(enc[i])) + "{0:04b}".format(ALPHABET.index(enc[i+1]))
        dec += chr(int(binary, 2))
    return dec

enc = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
for key in ALPHABET:
    flag = ""
    print("Key:", key)
    for c in enc:
        flag += shift(c, key)
    print("Flag: ", b16_decode(flag))