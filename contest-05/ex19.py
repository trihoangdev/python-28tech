def rev1(a, n):
    a.reverse()
    for x in a:
        print(x, end=' ')


def rev2(a, n):
    b = a[::-1]
    for x in b:
        print(x, end=' ')


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    rev2(a, n)
