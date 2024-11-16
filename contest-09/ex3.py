if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    max = -10 ** 9
    min = 10 ** 9
    for i in range(n):
        for j in range(m):
            if a[i][j] > max:
                max = a[i][j]
            if a[i][j] < min:
                min = a[i][j]
    print(min)
    for i in range(n):
        for j in range(m):
            if a[i][j] == min:
                print(i+1,j+1)
    print(max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max:
                print(i+1,j+1)
