from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    d = dict(Counter(a))
    for i in range(q):
        thao_tac, x = map(int, input().split())
        if thao_tac == 1:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        elif thao_tac == 2:
            if x in d:
                if d[x] == 1:
                    d.pop(x)
                else:
                    d[x] -= 1
        else:
            if x in d:
                print('YES')
            else:
                print('NO')
