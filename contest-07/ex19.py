if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    left, right = 0, n - 1
    while left <= right:
        if a[left] + a[right] <= x:
            cnt += 1
            left += 1
            right -= 1
        else:
            cnt += 1
            right -= 1
    print(cnt)
