h, m = map(int, input().split())
hRemain = 24 - h
mRemain = 60 - m
print((hRemain - 1) * 60 + mRemain)
