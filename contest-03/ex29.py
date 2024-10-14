from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def sum_digit(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


def is_fibo(n):
    if n == 0 or n == 1:
        return True
    f0, f1 = 0, 1
    for i in range(2, 50):
        fn = f0 + f1
        if fn == n:
            return True
        if fn > n:
            return False
        f0, f1 = f1, fn
    return False


def print_fibo(n):
    for i in range(2, n):
        if is_prime(i) and is_fibo(sum_digit(i)):
            print(i, end=' ')


if __name__ == '__main__':
    n = int(input())
    print_fibo(n)
