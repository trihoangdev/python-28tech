def check(n):
    if n < 100 and n % 10 == 2 * (n // 10):
        return True
    last = n % 10
    n //= 10
    temp = n
    res = 0
    cnt = 0
    while n > 9:
        cnt += 1
        res = res * 10 + n % 10
        n //= 10
    if res == temp % (10 ** cnt) and (last == 2 * n or n == 2 * last):
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input())
    print('YES') if check(n) else print('NO')
