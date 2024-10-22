def f(n):
    if n != 0:
        f(n // 2)
        print(n % 2, end='')


if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
    else:
        f(n)
