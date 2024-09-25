a, b = map(int, input().split())
res = 1
for i in range(1,min(a, b) + 1):
    res *= i
print(res)
