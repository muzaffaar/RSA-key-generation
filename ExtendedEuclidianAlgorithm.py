def extended_euclid(a, b, d, x, y):
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    s = 1
    while b != 0:
        r = a % b
        q = a // b
        a, b = b, r
        x, y = x1, y1
        x1 = q * x1 + x0
        y1 = q * y1 + y0
        x0, y0 = x, y
        s = -s
    x = s * x0
    y = -s * y0
    d, x, y = a, x, y
    return d, x, y


def main():
    a = int(input("Please enter 1st number: "))
    b = int(input("Please enter 2nd number: "))
    print(extended_euclid(a, b, 0, 0, 0))


if __name__ == '__main__':
    main()
