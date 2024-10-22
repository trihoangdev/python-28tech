def sum(n):
    if n == 1:
        return -1
    if n % 2 == 0:
        return n + sum(n - 1)
    else:
        return -n + sum(n - 1)


if __name__ == '__main__':
    n = int(input())
    print(sum(n))
