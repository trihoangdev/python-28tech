def check(a, first, last):
    if first > last:
        return True
    if a[first] == a[last]:
        return check(a, first + 1, last - 1)
    else:
        return False


if __name__ == '__main__':
    n = int(input())
    elements = list(map(int, input().split()))
    print('YES') if check(elements, 0, n - 1) else print('NO')
