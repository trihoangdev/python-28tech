def f(n):
    if n != 0:
        f(n // 16)
        res = n % 16
        if res < 10:
            print(res, end='')
        elif res == 10:
            print('A', end='')
        elif res == 11:
            print('B', end='')
        elif res == 12:
            print('C', end='')
        elif res == 13:
            print('D', end='')
        elif res == 14:
            print('E', end='')
        elif res == 15:
            print('F', end='')


if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
    else:
        f(n)
