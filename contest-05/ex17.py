def check(a, n):
    first, last = 0, n - 1
    while first < last:
        if a[first] != a[last]:
            return False
        first += 1
        last -= 1
    return True


def check2(a):
    b = a[:]
    a.reverse()
    return b == a


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # print('YES') if check(a, n) else print('NO')
    print('YES') if check2(a) else print('NO')
