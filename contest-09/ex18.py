a = []
path = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    dem = 0
    for i in range(n):
        for j in range(m):
            check = True
            for x, y in path:
                i1 = x + i
                j1 = y + j
                if 0 <= i1 < n and 0 <= j1 < m:
                    if a[i1][j1] >= a[i][j]:
                        check = False
                        break
            if check:
                dem += 1
    print(dem)
