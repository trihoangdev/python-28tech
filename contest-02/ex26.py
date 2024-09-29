a, b, n = map(int, input().split())
# Cach 1:
'''
flag = False
for i in range(n + 1):
    for j in range(n + 1):
        if a * i + b * j == n:
            flag = True
            break
if flag:
    print('YES')
else:
    print('NO')
'''

# Cach 2
check = False
for i in range(0, n // a + 1):
    temp = n - a * i
    if temp % b == 0:
        check = True
if check:
    print('YES')
else:
    print('NO')
