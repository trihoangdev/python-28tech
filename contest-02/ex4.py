n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += 1.0 / i
print('{:.3f}'.format(sum))
