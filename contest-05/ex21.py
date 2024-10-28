if __name__ == '__main__':
    n, x, k = map(int, input().split())
    a = list(map(int, input().split()))
    a[k - 1:k - 1] = [x]
    for x in a:
        print(x, end=' ')
