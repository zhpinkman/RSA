import random
import math
import numpy as np
import sys
from tqdm import tqdm


def read_key(filename):
    with open(filename, 'r') as f:
        key = int(f.readline())
        n = int(f.readline())
        f.close()
    return key, n


def read_input_file(filename):
    with open(filename, 'rb') as f:
        plain_text = f.read()
        f.close()
    return plain_text


def find_number_of_output_bytes(n):
    n_byte = 8
    i = 1
    while True:
        if not (2**((i-1)*n_byte) < n <= 2**((i)*n_byte)):
            i += 1
        else:
            break
    return i


def generate_cipher(plain_text, e, n, C_len, out_file):
    with open(out_file, 'wb') as f:
        for byte in tqdm(plain_text):
            cipher = pow(byte, e, n)
            cipher = cipher.to_bytes(C_len, sys.byteorder)
            f.write(cipher)
        f.close()


e, n = read_key('public.key')
C_len = find_number_of_output_bytes(n)
print(C_len)
plain_text = read_input_file('input.txt')
generate_cipher(plain_text, e, n, C_len, 'input.txt.enc')
