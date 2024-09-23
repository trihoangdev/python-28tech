import math

n = int(input())
for i in range(1, math.isqrt(n) + 1):
    if i ** 2 <= n:
        print(i ** 2, end=' ')
