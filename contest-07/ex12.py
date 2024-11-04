def find_first(a, l, r, x):
    res = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            res = m
            r = m - 1
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return res


def find_last(a, l, r, x):
    res = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            res = m
            l = m + 1
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    length = len(a)
    cnt = 0
    for i in range(0, n):
        res = k - a[i]
        first = find_first(a, i + 1, len(a) - 1, res)
        last = find_last(a, i + 1, len(a) - 1, res)
        if first != -1 and last != -1:
            cnt += last - first + 1
    print(cnt)
