from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    d = dict(Counter(a))
    a1 = list(d)
    a1.sort()
    for x in a1:
        if x in d:
            print(x, d[x])
    print()
    for x in d:
        print(x, d[x])
