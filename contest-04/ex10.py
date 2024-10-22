def sum(n):
    res = 0
    for i in range(1, n + 1):
        res += 1 / i
    return res


if __name__ == '__main__':
    n = int(input())
    print('{:.3f}'.format(sum(n)))
