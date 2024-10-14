n = int(input())
if n < 2:
    print(-1)
else:
    if n % 2 == 0:
        # n chan
        print(n // 2)
        while n > 0:
            print(2, end=' ')
            n -= 2
    else:
        # n le
        print(n // 2)
        while n > 3:
            print(2, end=' ')
            n -= 2
        print(3)
