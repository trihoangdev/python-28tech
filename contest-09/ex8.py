if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    u, v = map(int, input().split())
    for i in range(n):
        a[i][u - 1], a[i][v - 1] = a[i][v - 1], a[i][u - 1]
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
