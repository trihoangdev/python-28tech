F = [0] * 1000001
F[1] = 0
F[2] = 1


def fibo():
    for i in range(3, 1000001):
        F[i] = F[i - 1] + F[i - 2] + F[i - 3]
        F[i] %= 10 ** 9 + 7


if __name__ == '__main__':
    t = int(input())
    fibo()
    while t > 0:
        n = int(input())
        print(F[n])
        t -= 1
