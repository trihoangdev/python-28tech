from math import *

a, b = map(int, input().split(" "))
print(a + b)
print(a - b)
print(a * b)
print("INVALID" if (b == 0) else "{:.4f}".format(a / b))
