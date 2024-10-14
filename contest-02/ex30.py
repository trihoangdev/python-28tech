n = int(input())
res = ''
for i in range(n):
    temp = int(input())
    if temp % 2 == 0:
        res += 'EVEN\n'
    else:
        res += 'ODD\n'
print(res)
