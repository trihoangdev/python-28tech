n = int(input())
tong = n if n < 10 else 0
while n >= 10:
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    n = tong
print(tong)
