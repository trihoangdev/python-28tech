def find_fibo(n):
    if n == 0 or n == 1:
        return 1
    f0, f1 = 0, 1
    for i in range(2, 100):
        fn = f0 + f1
        if fn >= n:
            return fn
        f0, f1 = f1, fn
    return 0


if __name__ == '__main__':
    n = int(input())
    print(find_fibo(n))
