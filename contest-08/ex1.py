from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # Cach 1: List
    '''
    a.sort()
    cnt = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            cnt += 1
    print(cnt)
    '''

    # Cach 2: Set
    '''
    b = set({})
    for x in a:
        b.add(x)
    print(len(b))
    '''

    # Cach 3:Dictionary
    '''
    c = dict({})
    for x in a:
        if x in c:
            c[x] += 1
        else:
            c[x] = 1
    print(len(c))
    '''

    # Cach 4: Dictionary vs Counter
    d = dict(Counter(a))
    print(len(d))
