if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    for i in range(n):
        if i % 2 != 0:
            a[i].reverse()
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
