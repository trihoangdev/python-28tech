if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # Cach 1:
    # ok = False
    # for i in range(n):
    #     if a[i] == x:
    #         ok = True
    #         a[i:i+1] = []
    #         break
    # if not ok:
    #     print('NOT FOUND')
    # else:
    #     for x in a:
    #         print(x, end=' ')

    # Cach 2:
    if x in a:
        a.pop(a.index(x))
        for x in a:
            print(x, end=' ')
    else:
        print('NOT FOUND')
