F = [0] * 1000001
F[1] = 1


def fibo():
    for i in range(2, 1000001):
        F[i] = F[i - 1] + F[i - 2]
        F[i] %= 10 ** 9 + 7


if __name__ == '__main__':
    t = int(input())
    fibo()
    while t > 0:
        n = int(input())
        print(F[n])
        t -= 1
