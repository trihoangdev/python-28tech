# a - so tien cua chai 1 lit
# b - so tien cua chai 2 lit
# n - so lit can mua
# yc: tim so tien nho nhat
n, a, b = map(int, input().split())
if a < b / 2:
    print(n * a)
elif n % 2 == 0:
    print(n // 2 * b)
else:
    print(n // 2 * b + a)
