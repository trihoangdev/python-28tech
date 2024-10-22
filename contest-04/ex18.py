def tong_chan(n):
    if n == 0:
        return n
    if n % 2 == 0:
        return n % 10 + tong_chan(n // 10)
    else:
        return tong_chan(n // 10)


def tong_le(n):
    if n == 0:
        return n
    if n % 2 != 0:
        return n % 10 + tong_le(n // 10)
    else:
        return tong_le(n // 10)


if __name__ == '__main__':
    n = int(input())
    print(tong_chan(n))
    print(tong_le(n))
