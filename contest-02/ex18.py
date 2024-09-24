n = int(input())
cnt = 0
while n > 0:
    temp = int(n % 10)
    # check snt
    if temp >= 2:
        check = True
        for i in range(2, temp):
            if temp % i == 0:
                check = False
                break
        if check:
            cnt += 1
    n //= 10
print(cnt)
