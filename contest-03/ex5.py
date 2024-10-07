import math


def totalNumOfNumber(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


def isSmithNumber(n):
    total_num = totalNumOfNumber(n)
    sum_of_prime = 0
    tmp = n
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                # print(i)
                sum_of_prime += totalNumOfNumber(i)
                n //= i
    if tmp == n:
        return False
    if n > 1:
        # print(n)
        sum_of_prime += totalNumOfNumber(n)
    # print('=============')
    # print(total_num)
    # print(sum_of_prime)
    return total_num == sum_of_prime


if __name__ == '__main__':
    n = int(input())
    print('YES') if isSmithNumber(n) else print('NO')
