if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 1000001
    for x in a:
        count[x] += 1
    print(count.index(max(count)), max(count))
