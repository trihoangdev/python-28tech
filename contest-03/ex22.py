from math import isqrt


def check(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            dem = 0
            while n % i == 0:
                dem += 1
                n //= i
            if dem == 1:
                return False
    if n != 1:
        return False
    return True


def solve(a, b):
    for i in range(a, b + 1):
        if check(i):
            print(i, end=' ')


if __name__ == '__main__':
    a, b = map(int, input().split())
    solve(a, b)
