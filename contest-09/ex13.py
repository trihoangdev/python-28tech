if __name__ == '__main__':
    n, m, p = map(int, input().split())
    a, b = [], []
    for _ in range(n):
        temp = list(map(int, input().split()))
        a.append(temp)
    for _ in range(m):
        temp = list(map(int, input().split()))
        b.append(temp)
    c = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            res = 0
            for k in range(m):
                res += a[i][k] * b[k][j]
            c[i][j] = res
    for i in range(n):
        for j in range(p):
            print(c[i][j], end=' ')
        print()
