def pos(a, l, r, x):
    res = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] < x:
            res = m
            l = m + 1
        else:
            r = m - 1
    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n):
        p1 = pos(a, i + 1, n - 1, k - a[i])
        if p1 != -1:
            res += p1 - i
    print(res)
