from sys import orig_argv

n = int(input())
# hinh 1
for i in range(n):
    for j in range(n):
        if j <= i:
            print('*', end='')
    print()
print()

# hinh 2
for i in range(n):
    for j in range(n):
        if j < n - i:
            print('*', end='')
    print()
print()

# hinh 3
for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()

# hinh 4
for i in range(n):
    for j in range(n):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()

# hinh 5
for i in range(n):
    for j in range(n):
        if i == j or j == 0 or i == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
