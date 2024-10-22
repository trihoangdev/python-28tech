c = input()

if c >= "a" and c <= "z":
    print("LOWER")
elif c >= "A" and c <= "Z":
    print("UPPER")
elif c >= "0" and c <= "9":
    print("DIGIT")
else:
    print("SPECIAL")
