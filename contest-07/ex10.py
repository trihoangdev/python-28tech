if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    do_cung = a[0]
    cnt = 1
    for i in range(1, n):
        if do_cung <= 0:
            break
        cnt += 1
        do_cung = min(do_cung - 1, a[i])
    print(cnt)
