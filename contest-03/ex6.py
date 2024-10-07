import math


def tong_uoc(n):
    sum = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum


if __name__ == '__main__':
    n = int(input())
    print(tong_uoc(n))
