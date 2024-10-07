import math


def square_number_in_range(a, b):
    can1 = int(math.ceil(math.sqrt(a)))
    for i in range(can1, math.isqrt(b) + 1):
        print(i ** 2, end=' ')


if __name__ == '__main__':
    a, b = map(int, input().split())
    square_number_in_range(a, b)
