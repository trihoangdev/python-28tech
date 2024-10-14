def gcd(a, b):
    if a == b:
        return a
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    a, b = map(int, input().split())
    gcd = gcd(a, b)
    lcm = (a * b) // gcd
    print(gcd, lcm)
