import ChineseRemainderTheorem
import MillerRabin
import ExtendedEuclidianAlgorithm
import FastExponentiation
import EuclidanAlgorithm
from random import randint


def key_Gen():
    flag1 = False
    flag2 = False
    while True:
        if not flag1:
            p = randint(3, 1000)
        if not flag2:
            q = randint(3, 1000)

        if MillerRabin.is_prime(p, 8):
            flag1 = True
        if MillerRabin.is_prime(q, 8):
            flag2 = True

        if p != q and flag1 == True and flag2 == True:
            break

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 0
    while True:
        x = randint(1, phi)
        if EuclidanAlgorithm.euclid(phi, x) == 1:
            e = x
            break

    d = 0
    x, y = 0, 0
    a = ExtendedEuclidianAlgorithm.extended_euclid(e, phi, d, x, y)
    d = a[1]  # if we shifted the position of phi and e, then a[2], the y value would be d

    if d < 0:
        d = d + phi
    return p, q, n, phi, e, d


def encrypt(m, e, n):
    c = FastExponentiation.fast_exponentiation(m, e, n)
    return c


def decrypt(c, d, p, q):
    m = ChineseRemainderTheorem.chinese_remainder_theorem(c, d, p, q)
    return m


def signature(m, d, p, q):
    s = ChineseRemainderTheorem.chinese_remainder_theorem(m, d, p, q)
    return s


def verify(s, e, n):
    m = FastExponentiation.fast_exponentiation(s, e, n)
    return m


def main():
    myKeySet = key_Gen()
    print(myKeySet)

    m = randint(1, 1000)
    print("The original message is: ", m)
    c = encrypt(m, myKeySet[4], myKeySet[2])
    print("The encrypted message is: ", c)
    dec_m = decrypt(c, myKeySet[5], myKeySet[0], myKeySet[1])
    print("The decrypted message is: ", dec_m)
    sig = signature(m, myKeySet[5], myKeySet[0], myKeySet[1])
    print("The signature is: ", sig)
    ver = verify(sig, myKeySet[4], myKeySet[2])
    print("The verified message is: ", ver)
    if ver == dec_m:
        print("The signature is correct!")
    else:
        print("The signature is incorrect!")


if __name__ == '__main__':
    main()
