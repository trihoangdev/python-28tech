from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def check(n):
    i = 2
    while i <= isqrt(n):
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                cnt += 1
                n //= i
                if cnt == 2:
                    return True
        i += 1
    return False


def solve(a, b):
    for i in range(a, b + 1):
        if check(i):
            print(i, end=' ')


if __name__ == '__main__':
    a, b = map(int, input().split())
    solve(a, b)
