from math import *


def cp(n):
    can = isqrt(n)
    return can * can == n


if __name__ == '__main__':
    n = int(input())
    print('YES') if cp(n) else print('NO')
