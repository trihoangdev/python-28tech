import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            return False
    return True


def isSphenic(n):
    cnt = 0
    i = 2
    while i <= math.isqrt(n) + 1:
        if n % i == 0:
            n //= i
            cnt += 1
            if n % i == 0:
                return False
        i += 1
    if n > 1:
        cnt += 1
    return cnt == 3

'''
def phantichSphenic(n):
    for i in range(2, math.isqrt(n) + 1):
        if isPrime(i) and n % i == 0:
            while n % i == 0:
                print(i, end=' ')
                n //= i
    if n > 1:
        print(n)
    else:
        print()
'''

if __name__ == '__main__':
    n = int(input())
    # phantichSphenic(n)
    print(1) if isSphenic(n) else print(0)
