def sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum(n // 10)


if __name__ == '__main__':
    n = int(input())
    print(sum(n))
