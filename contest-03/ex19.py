from math import isqrt


# def check(n):
#     sum = 1
#     for i in range(2, isqrt(n) + 1):
#         if n % i == 0:
#             sum += i
#             sum += n // i
#     return n == sum

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def check(n):
    for i in range(2, 32):
        if is_prime(i) and is_prime(2 ** i - 1):
            if (2 ** i - 1) * (2 ** (i - 1)) == n:
                return True
    return False


if __name__ == '__main__':
    n = int(input())
    print('YES') if check(n) else print('NO')
