k2, k3, k5, k6 = map(int, input().split())
max256 = min(k2, k5, k6)
sum = 0
sum += max256 * 256
max32 = min(k2 - max256, k3)
if max32 > 0:
    sum += max32 * 32
print(sum)
