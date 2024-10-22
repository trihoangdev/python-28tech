c = input()
if c == "z" or c == "Z":
    print("a")
else:
    c = chr(ord(c[0]) + 1).lower()
    print(c)
