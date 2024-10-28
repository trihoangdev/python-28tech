if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 10 ** 7
    for x in a:
        b[x] += 1
    l, r = min(a), max(a)
    for x in a:
        if b[x] != 0:
            print(x, end=' ')
            b[x] = 0
