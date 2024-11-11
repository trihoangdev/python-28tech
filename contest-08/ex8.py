if __name__ == '__main__':
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s1 = set(a)
    s2 = set(b)
    s3 = s1.union(s2)
    s4 = s1.intersection(s2)
    s5 = list(s3.difference(s4))
    s5.sort()
    for x in s5:
        print(x, end=' ')
