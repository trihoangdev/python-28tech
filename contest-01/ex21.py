from math import *

a, b, k = map(int, input().split())
print(ceil(k / 2) * a - floor(k / 2) * b)
