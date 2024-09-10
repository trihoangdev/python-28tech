c = input()
if (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):
    if c >= "a" and c <= "z":
        print(c.upper())
    else:
        print(c.lower())
else:
    print(c)
