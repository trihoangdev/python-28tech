import math


def square_number_in_range(a, b):
    can1 = math.isqrt(a)
    can2 = math.isqrt(b)
    if can1 * can1 != a:
        can1 += 1
    if (can2 + 1) * (can2 + 1) == b:
        can2 += 1
    return can2 - can1 + 1


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(square_number_in_range(a, b))
