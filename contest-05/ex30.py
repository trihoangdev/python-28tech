if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 1000001
    for x in a:
        count[x] += 1
    max_fre, res = 0, 0
    for x in a:
        if count[x] > max_fre:
            max_fre, res = count[x], x
    print(res, max_fre)
