# 1. Tìm vị trí xuất hiện đầu tiên của phần tử X trong mảng, nếu không tồn tại X in ra -1.
def find_first_index(a, l, r, x):
    index = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            index = m
            r = m - 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return index


# 2. Tìm vị trí xuất hiện cuối cùng của phần tử X trong mảng, nếu không tồn tại X in ra -1.
def find_last_index(a, l, r, x):
    index = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            index = m
            l = m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return index


# 3. Tìm vị trí xuất hiện đầu tiên của phần tử >= X trong mảng, nếu không tồn tại phần tử >=X in ra -1.
def find_first_index1(a, l, r, x):
    index = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] >= x:
            index = m
            r = m - 1
        else:
            l = m + 1
    return index


# 4. Tìm vị trí xuất hiện đầu tiên của phần tử > X trong mảng, nếu không tồn tại phần tử >X in ra -1.
def find_first_index2(a, l, r, x):
    index = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] > x:
            index = m
            r = m - 1
        else:
            l = m + 1
    return index


# 5. Tìm số lần xuất hiện của phần tử X trong mảng sử dụng kết quả của hàm 1 và 2.
def find_frequency_X(a, l, r, x):
    return find_last_index(a, l, r, x) - find_first_index(a, l, r, x) + 1


if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(find_first_index(a, 0, len(a) - 1, x))
    print(find_last_index(a, 0, len(a) - 1, x))
    print(find_first_index1(a, 0, len(a) - 1, x))
    print(find_first_index2(a, 0, len(a) - 1, x))
    print(find_frequency_X(a, 0, len(a) - 1, x))
