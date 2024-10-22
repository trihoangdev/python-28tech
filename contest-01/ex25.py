n = int(input())
res = 0
if n % 100 >= 0:
    res += n // 100
    n %= 100

if n % 20 >= 0:
    res += n // 20
    n %= 20

if n % 10 >= 0:
    res += n // 10
    n %= 10

if n % 5 >= 0:
    res += n // 5
    n %= 5

res += n
n = 0
print(res)
