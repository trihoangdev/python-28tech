if __name__ == '__main__':
    m, n = map(int, input().split())
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))
    c = list(a.union(b))
    c.sort(reverse=True)
    for x in c:
        print(x, end=' ')
