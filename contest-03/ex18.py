def check(n):
    for i in range(1, (n // 111) + 1):
        if (n - 111 // i) % 11 == 0:
            return True
    return False


if __name__ == '__main__':
    n = int(input())
    print('YES') if check(n) else print('NO')
