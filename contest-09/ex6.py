if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    dcc, dcp = 0, 0
    for i in range(n):
        a[i][i], a[i][n - i - 1] = a[i][n - i - 1], a[i][i]
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
