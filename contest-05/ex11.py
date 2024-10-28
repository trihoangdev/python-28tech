def is_fibo(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    f0, f1 = 0, 1
    for i in range(100):
        fn = f1 + f0
        if fn == n:
            return True
        elif fn > n:
            return False
        f0, f1 = f1, fn
    return False


F = [0] * 100


def fibo():
    F[0] = 0
    F[1] = 1
    for i in range(2, 100):
        F[i] = F[i - 1] + F[i - 2]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    fibo()
    ok = False
    for x in a:
        if x in F:
            ok = True
            print(x, end=' ')
    if not ok:
        print('NONE')
