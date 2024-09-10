from math import *

a1, a2, a3, b1, b2, b3 = map(int, input().split())
n = int(input())
sum_cup = a1 + a2 + a3
sum_hc = b1 + b2 + b3
if ceil(sum_cup / 5) + ceil(sum_hc / 10) <= n:
    print("YES")
else:
    print("NO")
