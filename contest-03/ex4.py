import math


def largestPrime(n):
    last = 1
    i = 2
    while i < math.isqrt(n) + 1:
        if n % i == 0:
            last = i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        return n
    else:
        return last


if __name__ == '__main__':
    n = int(input())
    while n != 0:
        a = int(input())
        print(largestPrime(a))
        n -= 1
