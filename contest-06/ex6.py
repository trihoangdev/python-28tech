from math import isqrt

prime = [True] * (10 ** 6 + 1)


def seive():
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(10 ** 6) + 1):
        if prime[i]:
            for j in range(i * i, 10 ** 6 + 1, i):
                prime[j] = False


if __name__ == '__main__':
    seive()
    F = [0] * (10 ** 6 + 1)
    tich = 1
    for i in range(2, 10 ** 6 + 1):
        if prime[i]:
            tich *= i
            tich %= 10 ** 9 + 7
        F[i] = tich
    t = int(input())
    while t > 0:
        n = int(input())
        print(F[n])
        t -= 1
