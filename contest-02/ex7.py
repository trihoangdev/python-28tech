n = int(input())
res = ''
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        res = res + ' ' + str(i)
print(count)
print(res.strip())
