from math import isqrt

prime = [True] * 1000001


def seive():
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(10 ** 6) + 1):
        # Kiểm tra nếu i là SNT thì loại bội của i
        if prime[i]:
            # Duyệt bội từ i^2
            for j in range(i ** 2, 10 ** 6 + 1, i):
                prime[j] = False


if __name__ == '__main__':
    seive()
    t = int(input())
    F = [0] * (10 ** 6 + 1)
    F[0], F[1] = 0, 0
    dem = 0
    for i in range(2, 10 ** 6 + 1):
        if prime[i]:
            dem += 1
        F[i] = dem
    while t > 0:
        n = int(input())
        print(F[n])
        t -= 1
