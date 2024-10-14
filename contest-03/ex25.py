def gcd(a, b):
    if a == b:
        return a
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        j = i + 1
        while i < j <= b:
            if gcd(i, j) == 1:
                print('(', i, ',', j, ')', sep='')
            j += 1
