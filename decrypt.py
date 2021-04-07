import math
import numpy
import random
import sys
from tqdm import tqdm


def read_key(filename):
    with open(filename, 'r') as f:
        key = int(f.readline())
        n = int(f.readline())
        f.close()
    return key, n


def read_cipher_text(filename):
    with open(filename, 'rb') as f:
        cipher_text = f.read()
        f.close()
    return cipher_text


def find_number_of_output_bytes(n):
    n_byte = 8
    i = 1
    while True:
        if not (2**((i-1)*n_byte) < n <= 2**((i)*n_byte)):
            i += 1
        else:
            break
    return i


def decrypt_cipher(cipher_text, d, n, C_len, out_file):
    decrypted_result = []
    for i in tqdm(range(int(len(cipher_text) / C_len))):
        block = bytearray([cipher_text[j]
                           for j in range(C_len*i, C_len*i+C_len)])
        block_int = int.from_bytes(block, sys.byteorder)
        decrypted_block = pow(block_int, d) % n
        decrypted_result.append(decrypted_block)

    # plain_text = ''.join([chr(ascii_byte) for ascii_byte in decrypted_result])
    with open(out_file, 'wb') as f:
        f.write(bytes(decrypted_result))
        f.close()


d, n = read_key('private.key')
C_len = find_number_of_output_bytes(n)
print(C_len)
cipher_text = read_cipher_text('input.txt.enc')
decrypt_cipher(cipher_text, d, n, C_len, 'output.txt')
