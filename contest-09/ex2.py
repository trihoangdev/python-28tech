if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    sum_row = [0] * n
    sum_cel = [0] * m
    for row in range(n):
        sum_row[row] = sum(a[row])
        for cel in range(m):
            sum_cel[cel] += a[row][cel]
    for x in sum_row:
        print(x, end=' ')
    print()
    for x in sum_cel:
        print(x, end=' ')
