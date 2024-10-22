a, b, c, d = map(float, input().split())
agv = (a + b + c * 2 + d * 3) / 7
if agv >= 8:
    print("GIOI")
elif agv >= 6.5:
    print("KHA")
elif agv >= 5:
    print("TRUNG BINH")
else:
    print("YEU")
