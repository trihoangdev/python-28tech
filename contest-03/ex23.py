from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(2, n // 2 + 1):
            if is_prime(i) and is_prime(n - i):
                print(i, n - i)