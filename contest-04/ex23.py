def check(a, n, index):
    if index == n:
        return True
    if a[index] % 2 == 0:
        return check(a, n, index + 1)
    else:
        return False


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print('YES') if check(a, n, 0) else print('NO')
