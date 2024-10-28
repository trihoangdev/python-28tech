if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 1000001
    for x in a:
        count[x] += 1
    cnt = 0
    for x in a:
        if count[x] > 0:
            cnt += 1
            count[x] = 0
    print(cnt)
