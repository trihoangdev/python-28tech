def gcd(a, b):
    if a == b:
        return a
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    uc = 0
    for i in range(0, n):
        uc = gcd(uc, a[i])
    print(uc)
