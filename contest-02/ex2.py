n = int(input())
sum = 0
#print(n*(n+1)*(2*n+1)//6)
for i in range(1, n + 1):
    sum += i ** 2
print(sum)
