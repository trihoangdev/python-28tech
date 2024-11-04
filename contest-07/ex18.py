if __name__ == '__main__':
    n, s = map(int, input().split())
    a = []
    for i in range(n):
        x = list(map(int, input().split()))
        a.append(x)
    a.sort(key=lambda x: x[0])
    win = True
    for i in range(n):
        if s < a[i][0]:
            win = False
            break
        else:
            s += a[i][1]
    print('YES') if win else print('NO')
