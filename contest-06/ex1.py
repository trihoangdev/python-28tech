F = [1] * 1000001


def gt():
    for i in range(2, 1000001):
        F[i] = F[i - 1] * i
        F[i] %= 10 ** 9 + 7


if __name__ == '__main__':
    t = int(input())
    gt()
    while t > 0:
        n = int(input())
        print(F[n])
        t -= 1
