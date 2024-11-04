def pos(a, l, r, x):
    res = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] > x:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        p = pos(a, i + 1, n - 1, k - a[i])
        if p != -1:
            cnt += n - p
    print(cnt)
