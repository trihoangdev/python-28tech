def max_digit(n):
    if n < 10:
        return n
    else:
        return max(n % 10, max_digit(n // 10))


def min_digit(n):
    if n < 10:
        return n
    else:
        return min(n % 10, min_digit(n // 10))


if __name__ == '__main__':
    n = int(input())
    print(max_digit(n), min_digit(n))
