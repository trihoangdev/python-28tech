"""
d1: khoảng cách từ nhà đến CH1
d2: khoảng cách từ nhà đến CH2
d3: khoảng cách giữa 2 CH
"""

d1, d2, d3 = map(int, input().split())
print(min((d1 + d2 + d3), 2 * (d1 + d3), 2 * (d1 + d2), 2 * (d2 + d3)))
