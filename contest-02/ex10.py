n = int(input())
n_arr = list(map(int, input().split()))
flag = False
for i in range(0,n):
    if n_arr[i] == 2022:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')
