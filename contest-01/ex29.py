a, b, c, d = map(int, input().split())
if b % a == 0:
    bs = b // a
    if b * bs != c:
        print("NO")
    elif c * bs != d:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
