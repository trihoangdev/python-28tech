if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * (10 ** 6 + 1)
    for x in a:
        b[x] = 1
    cnt = 0
    l, r = a[0], a[n - 1]
    for i in range(l, r + 1):
        if b[i] == 0:
            cnt += 1
    print(cnt)
