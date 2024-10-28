from math import *


def nt(x):
    if x < 2:
        return False
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n - 1):
        tong_trai, tong_phai = 0, 0
        for j in range(0, n):
            if j < i:
                tong_trai += a[j]
            elif j > i:
                tong_phai += a[j]
        if nt(tong_phai) and nt(tong_trai):
            print(i, end=' ')
