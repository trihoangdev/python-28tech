n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += 1.0 / (2 * i)
print('{:.5f}'.format(sum))