import ExtendedEuclidianAlgorithm
import FastExponentiation


def chinese_remainder_theorem(c, d, p, q):
    c1 = FastExponentiation.fast_exponentiation(c, d % (p - 1), p)
    c2 = FastExponentiation.fast_exponentiation(c, d % (q - 1), q)
    M = p * q
    M1 = q
    M2 = p
    gcd, y1, y2 = ExtendedEuclidianAlgorithm.extended_euclid(M1, M2, 0, 1, 0)
    m = c1 * M1 * y1 + c2 * M2 * y2
    while m < 0:
        m = m + M
    if m > M:
        m = m % M
    return m


def main():
    print(chinese_remainder_theorem(42, 2753, 151, 157))


if __name__ == '__main__':
    main()
