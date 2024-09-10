n = int(input())
# 1
print("YES" if n % 2 == 0 else "NO")
# 2
print("YES" if n % 3 == 0 and n % 5 == 0 else "NO")
# 3
print("YES" if n % 3 == 0 and n % 7 != 0 else "NO")
# 4
print("YES" if n % 3 == 0 or n % 7 == 0 else "NO")
# 5
print('YES' if n > 30 and n < 50 else 'NO')
# 6
print("YES" if n >= 30 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0) else "NO")
# 7
print(
    "YES"
    if n >= 10
    and n <= 99
    and ((n % 10) == 3 or (n % 10) == 5 or (n % 10) == 7 or (n % 10) == 2)
    else "NO"
)
# 8
print("YES" if (n <= 100 and n % 23 == 0) else "NO")
# 9
print("YES" if (n > 20 or n < 10) else "NO")
# 10
print("YES" if ((n % 10) % 3 == 0) else "NO")
