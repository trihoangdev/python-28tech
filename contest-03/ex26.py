def fibo(n):
    f0 = 0
    f1 = 1
    i = 2
    print(1, sep='\n')
    while i < n + 1:
        fn = f0 + f1
        print(fn)
        f0, f1 = f1, fn
        i += 1


if __name__ == '__main__':
    n = int(input())
    fibo(n)
