import math


def is_square_number(n):
    return math.isqrt(n) * math.isqrt(n) == n


if __name__ == '__main__':
    n = int(input())
    print('YES') if is_square_number(n) else print('NO')
