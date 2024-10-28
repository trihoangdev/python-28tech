from math import *


def nt(x):
    if x < 2:
        return False
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True


def do_something(a, n):
    tong = 0
    cnt = 0
    for x in a:
        if nt(x):
            tong += x
            cnt+=1
    return tong / cnt


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print("{:.3f}".format(do_something(a, n)))
