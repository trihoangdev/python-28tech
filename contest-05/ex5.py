if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if i % 2 == 0 and a[i] % 2 == 0:
            cnt += 1
            print(a[i], end=' ')
    if cnt == 0:
        print('NONE')
