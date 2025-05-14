from random import randint

probablyPrime = True
composite = False


def power_mod(b, e, m):
    x = 1
    while e > 0:
        if e % 2 == 1:
            x = (b * x) % m
        b = (b * b) % m
        e = e // 2
    return x


def is_strong_pseudo_prime(n, a):
    # formula: p-1 = 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s = s + 1
    t = power_mod(a, d, n)
    if t == 1:
        return probablyPrime
    while s > 0:
        if t == n - 1:
            return probablyPrime
        t = (t * t) % n
        s = s - 1
    return composite


def is_prime(n, k):
    for i in range(1, k + 1):
        a = randint(2, n - 1)
        if not is_strong_pseudo_prime(n, a):
            return composite
    return probablyPrime


def main():
    a = int(input("Enter the number: "))
    if is_prime(a, 17):
        print("The number provided is probably a prime\n")
    else:
        print("The number provided is a composite\n")


if __name__ == '__main__':
    main()
