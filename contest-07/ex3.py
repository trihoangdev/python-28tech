from functools import cmp_to_key


def sum_digit(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res


def cmp(a, b):
    tong1, tong2 = sum_digit(a), sum_digit(b)
    if tong1 != tong2:
        return tong1 - tong2
    else:
        return a - b


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (sum_digit(x), x))
    for x in a:
        print(x, end=' ')
