n = int(input())
res = 1
for i in range(1, n):
    gt = 1
    for j in range(1, i + 1):
        gt *= j
    res += 1 / gt
print('{:.4f}'.format(res))
