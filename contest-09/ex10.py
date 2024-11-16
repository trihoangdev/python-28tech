from math import isqrt


def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    s = set({})
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1:
                if nt(a[i][j]):
                    s.add(a[i][j])
    print(len(s))
