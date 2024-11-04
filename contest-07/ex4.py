if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    min_index = 10 ** 18
    for i in range(1, n):
        min_index = min(min_index, a[i] - a[i - 1])
    print(min_index)
