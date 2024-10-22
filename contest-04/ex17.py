def plr(n):
    if n <= 0:
        return
    else:
        print(n % 10, end=' ')
        plr(n // 10)


def prl(n):
    if n > 0:
        prl(n // 10)
        print(n % 10, end=' ')


if __name__ == '__main__':
    n = int(input())
    prl(n)
    print()
    plr(n)

