def fast_exponentiation(base, exp, mod):
    base = base % mod
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif exp % 2 == 0:
        return fast_exponentiation(base * base % mod, exp / 2, mod)
    else:
        return base * fast_exponentiation(base, exp - 1, mod) % mod


def main():
    print(fast_exponentiation(7, 66, 101))


if __name__ == '__main__':
    main()
