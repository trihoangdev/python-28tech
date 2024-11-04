if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    a.sort(reverse=True)
    for i in range(n):
        a[i] -= i
        if a[i] <= 0:
            break
        res += a[i]
    print(res)
