if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 1000001
    for x in a:
        count[x] += 1
    for x in a:
        if count[x] > 0:
            print(x, count[x])
            count[x] = 0
