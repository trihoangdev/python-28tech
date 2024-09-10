n = int(input())
if n >= 365:
    print(int(n / 365), end=" ")
    n = int(n % 365)
    if n >= 7:
        print(int(n / 7), end=" ")
        n = int(n % 7)
        print(n)
    else:
        print(0, end=" ")
        print(n)
elif n >= 7:
    print(0, int(n / 7), end=" ")
    n = int(n % 7)
    print(n)
else:
    print(0, 0, n)
