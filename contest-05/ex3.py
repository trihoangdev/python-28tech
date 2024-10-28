if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    min = 10 ** 7
    for x in a:
        if x < min:
            min = x
            cnt = 1
            continue
        if x == min:
            cnt += 1
    print(cnt)
