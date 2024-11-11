if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    s = set({})
    F = [0] * n
    F[n - 1] = 1
    s.add(a[n - 1])
    for i in range(n - 2, -1, -1):
        if a[i] in s:
            F[i] = F[i + 1]
        else:
            s.add(a[i])
            F[i] = F[i + 1] + 1
    for _ in range(q):
        x = int(input())
        print(F[x])
