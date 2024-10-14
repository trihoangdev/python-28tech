n = int(input())
if n == 0:
    print(1)
else:
    cnt = 0
    while n > 0:
        n //= 10
        cnt += 1
    print(cnt)
