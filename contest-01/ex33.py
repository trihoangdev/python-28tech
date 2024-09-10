a, b, c, n = map(int, input().split())
if (a + b + c + n) % 3 == 0:
    avg = (a + b + c + n) / 3
    if a <= avg and b <= avg and c <= avg:
        print('YES')
    else:
        print('NO')
else:
    print('NO')