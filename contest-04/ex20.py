def f(n):
    if n == 1:
        return 0
    t1, t2, t3 = 10 ** 9, 10 ** 9, 10 ** 9
    if n % 2 == 0:
        t1 = 1 + f(n // 2)
    if n % 3 == 0:
        t2 = 1 + f(n // 3)
    if n > 1:
        t3 = 1 + f(n - 1)
    return min(t1, t2, t3)


if __name__ == '__main__':
    n = int(input())
    print(f(n))
