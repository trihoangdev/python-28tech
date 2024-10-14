from math import *


def sum_prime_digit(n):
    res = 0
    while n != 0:
        digit = n % 10
        if digit == 2 or digit == 3 or digit == 5 or digit == 7:
            res += digit
            n //= 10
        else:
            return False
    return is_prime(res)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def num_of_perfect_prime(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if sum_prime_digit(i) and is_prime(i):
            cnt += 1
    return cnt


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(num_of_perfect_prime(a, b))
