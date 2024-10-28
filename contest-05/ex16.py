from math import *


def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def cp(n):
    return isqrt(n) * isqrt(n) == n


def tn(n):
    temp = n
    res = 0
    while n != 0:
        res = res * 10 + n % 10
        n //= 10
    return res == temp


def sum_digits(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count_nt, count_cp, count_digit, count_tn = 0, 0, 0, 0
    for x in a:
        if nt(x): count_nt += 1
        if cp(x): count_cp += 1
        if tn(x): count_tn += 1
        if nt(sum_digits(x)): count_digit += 1
    print(count_nt, count_tn, count_cp, count_digit, sep='\n')
