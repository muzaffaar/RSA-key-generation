def euclid(a, b):
    d = 0
    while b != 0:
        d = a
        a = b
        b = d % a
    return a


def main():
    a = int(input("Enter First Number: "))
    b = int(input("Enter the second number: "))
    print(euclid(a, b))


if __name__ == '__main__':
    main()
