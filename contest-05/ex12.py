if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    max_index, min_index, max, min = 0, 0, a[0], a[0]
    for i in range(0, n):
        if a[i] > max:
            max = a[i]
            max_index = i
        elif a[i] <= min:
            min = a[i]
            min_index = i
    print(min_index, max_index)
