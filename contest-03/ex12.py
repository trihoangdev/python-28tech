import math


def is_rev_num(n):
    res = 0
    temp = n
    while n != 0:
        res = res * 10 + n % 10
        n //= 10
    return res == temp


def is_has_3_prime(n):
    i = 2
    cnt = 0
    while i < math.isqrt(n) + 1:
        if n % i == 0:
            cnt += 1
            if cnt > 3:
                return True
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        cnt += 1
    return cnt == 3


if __name__ == '__main__':
    a, b = map(int, input().split())
    dem = 0
    for i in range(a, b + 1):
        if is_has_3_prime(i) and is_rev_num(i):
            print(i, end=' ')
            dem += 1
    if dem == 0:
        print(-1)
