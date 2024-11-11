if __name__ == '__main__':
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    a1 = set(a)
    b = list(map(int, input().split()))
    b1 = set(b)
    c = list(a1.difference(b1))
    c.sort()
    for x in c:
        print(x, end=' ')
