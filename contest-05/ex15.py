if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    max1, max2 = 0, 0
    for x in a:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
    print(max1, max2)
