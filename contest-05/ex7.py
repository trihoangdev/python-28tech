if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    min = 10 ** 7
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(a[i] - a[j]) < min:
                min = abs(a[i] - a[j])
    print(min)
