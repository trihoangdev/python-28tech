from sys import orig_argv

n = int(input())
# hinh 1
cnt1 = 1
for i in range(n):
    for j in range(n):
        print(cnt1, end=' ')
        cnt1 += 1
    print()
print()

# hinh2
for i in range(n):
    cnt2 = i + 1
    for j in range(n):
        print(cnt2, end=' ')
        cnt2 += 1
    print()
print()

# hinh3
for i in range(n):
    for j in range(n, 0, -1):
        if j > i + 1:
            print('~', end='')
        else:
            print(i + 1, end='')
    print()
print()

# hinh4
for i in range(1, n + 1):
    cnt4 = i
    for j in range(1, n + 1):
        if j <= i:
            print(cnt4, end=' ')
            cnt4 += n - j
        else:
            print('', end=' ')
    print()
