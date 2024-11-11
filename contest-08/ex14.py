from collections import Counter
from math import isqrt


def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    a = list(map(int, input().split()))
    d = dict({})
    for x in a:
        if nt(x):
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
    for val, fre in d.items():
        print(val, fre)
