n = int(input())
chaiBia = n // 28
vo = chaiBia
while chaiBia >= 3:
    # update chaiBia
    chaiBia -= 3
    chaiBia += 1
    vo += 1
print(vo)
