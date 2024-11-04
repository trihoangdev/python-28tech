if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a[1:] = sorted(a[1:], reverse=True)
    ans = a[0]
    i = 1
    while i < n:
        if i <= k:
            ans += a[i]
        else:
            ans -= a[i]
        i += 1
    print(ans)
