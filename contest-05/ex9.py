if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 10 ** 3
    for x in a:
        b[x] += 1
    for x in a:
        if b[x] != 0:
            print(x, b[x])
            b[x] = 0
