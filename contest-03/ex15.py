import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def is_last_digit_largest(n):
    last = n % 10
    while n != 0:
        if n % 10 > last:
            return False
        n //= 10
    return True


if __name__ == '__main__':
    n = int(input())
    count = 0
    for i in range(2, n + 1):
        if is_last_digit_largest(i) and is_prime(i):
            count += 1
            print(i, end=' ')
    print()
    print(count)
