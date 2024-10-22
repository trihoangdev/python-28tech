def check(n):
    if n % 2 != 0:
        return False
    if n == 0:
        return True
    return check(n // 10)


if __name__ == '__main__':
    n = int(input())
    print('YES') if check(n) else print('NO')
