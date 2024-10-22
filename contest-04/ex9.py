def binpow(a, b):
    if b == 0:
        return 1
    X = binpow(a, b // 2)
    if b % 2 == 0:
        return (X * X) % (10 ** 9 + 7)
    else:
        return (X * X * a) % (10 ** 9 + 7)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(binpow(a, b))
