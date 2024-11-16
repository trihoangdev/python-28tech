def is_reverse_num(n):
    if n < 10:
        return True
    temp = n
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return temp == rev


if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    cnt = 0
    for i in range(n):
        for j in range(i + 1):
            if is_reverse_num(a[i][j]):
                cnt += 1
    print(cnt)
