if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if i == 0:
            if a[0] * a[1] < 0:
                print(a[i], end=' ')
        elif i == n - 1:
            if a[-1] * a[-2] < 0:
                print(a[i], end=' ')
        else:
            if a[i] * a[i + 1] < 0 or a[i] * a[i - 1] < 0:
                print(a[i], end=' ')
