def is_fibo(n):
    if n == 0 or n == 1:
        return True
    f0, f1 = 0, 1
    for i in range(2, 100):
        fn = f0 + f1
        if fn == n:
            return True
        if fn > n:
            return False
        f0, f1 = f1, fn
    return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print('YES') if is_fibo(n) else print('NO')
