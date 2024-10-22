def count(n):
    if n < 10:
        return n
    else:
        return count(n // 10)


if __name__ == '__main__':
    n = int(input())
    print(count(n))
