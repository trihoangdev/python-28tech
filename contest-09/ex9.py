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
    cnt = 0
    for i in range(n):
        for j in range(n):
            if (i == j or j == (n - i - 1)) and nt(a[i][j]):
                cnt += 1
    # if n % 2 != 0:
    #     if nt(a[n // 2 + 1][n // 2 + 1]):
    #         cnt -= 1
    print(cnt)
