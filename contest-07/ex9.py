if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    # 1 2 7 8 9
    # 3 4 4 5 8
    cnt, ia, ib = 0, 0, 0
    while ia < n and ib < m:
        if a[ia] > b[ib]:
            cnt += 1
            ia += 1
            ib += 1
        elif a[ia] <= b[ib]:
            ia += 1
    print(cnt)
