def plr(a, index):
    if index == len(a):
        return
    print(a[index], end=' ')
    plr(a, index + 1)


def prl(a, index):
    if index == -1:
        return
    print(a[index], end=' ')
    prl(a, index - 1)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    plr(a, 0)
    print()
    prl(a, len(a) - 1)
