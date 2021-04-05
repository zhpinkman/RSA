import math
import numpy as np
import random
import sys


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):

    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


def write_key(key, filename):
    with open(filename, 'w') as fp:
        fp.write(str(key[0]))
        fp.write('\n')
        fp.write(str(key[1]))
        fp.close()


def generate_keypairs(p, q):
    if not(is_prime(p) and is_prime(q)):
        print('Both numbers you are entering must be prime!')
        return -1
    if p == q:
        print('Numbers you are are entering must be not the same!')
        return -1
    n = p * q
    if n < 256:
        print('The multiplication of two numbers entered must be greater than 256!')
        return -1

    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)

    g1 = gcd(e, phi)
    g2 = gcd(e, n)
    while g1 != 1 or g2 != 1:
        e = random.randrange(2, phi)
        g1 = gcd(e, phi)
        g2 = gcd(e, n)

    d = extended_gcd(e, phi)[1]
    d += phi
    while d < 0:
        d += phi
    print('p: {}, q: {}, n: {}, phi: {}, e: {}, d: {}'.format(p, q, n, phi, e, d))

    write_key((e, n), 'public.key')
    write_key((d, n), 'private.key')

    return ((e, n), (d, n))


# generate_keypairs(2, 4)
# generate_keypairs(3, 3)
# generate_keypairs(2, 7)

p = int(input('enter the first prime number p: '))
q = int(input('enter the second prime numberq: '))
generate_keypairs(p, q)
