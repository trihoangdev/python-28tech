def gcd(a, b):
    if a == b:
        return a
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def check(x, y, z, n):
    bc = lcm(lcm(x, y), z)
    tmp = 10 ** (n - 1)
    ans = (tmp + bc - 1) // bc * bc
    if ans < 10 ** n:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    x, y, z, n = map(int, input().split())
    check(x, y, z, n)
