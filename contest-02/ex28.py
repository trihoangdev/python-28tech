n = int(input())
tong = 0
'''
for i in range(1, n + 1):
    gt = 1
    for j in range(1, i + 1):
        gt *= j
    tong += gt
print(tong)
'''

# Cach ngan hon
gt = 1
for i in range(1, n + 1):
    gt *= i
    tong += gt
print(tong)
