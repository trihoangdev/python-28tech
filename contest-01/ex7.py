import math
a, b = map(int, input().split(' '))
print(a // b * b)
print(math.ceil(a / b) * b)
