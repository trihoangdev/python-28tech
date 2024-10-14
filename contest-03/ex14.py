def lp(n):
    tong = 0
    check6 = False
    rev = 0
    temp = n
    while n != 0:
        rev = rev * 10 + n % 10
        if n % 10 == 6:
            check6 = True
        tong += n % 10
        n //= 10
    return check6 and (rev == temp) and (tong % 10 == 8)


if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if lp(i):
            print(i, end=' ')
