def find(a, l, r, x):
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return 1
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ok = False
    for i in range(n):
        if find(a, i + 1, n - 1, a[i] - x) == 1:
            ok = True
            break
    if not ok:
        print(-1)
    else:
        print(1)
