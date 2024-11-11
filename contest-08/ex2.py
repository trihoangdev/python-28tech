# Cach 1: Set
# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, input().split()))
#     q = int(input())
#     s = set({})
#     for x in a:
#         s.add(x)
#     for i in range(q):
#         x = int(input())
#         if x in s:
#             print('YES')
#         else:
#             print('NO')

# Cách 2: Dictionary
# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, input().split()))
#     q = int(input())
#     m = dict({})
#     for x in a:
#         if x in m:
#             m[x] += 1
#         else:
#             m[x] = 1
#     for i in range(q):
#         x = int(input())
#         if x in m:
#             print('YES')
#         else:
#             print('NO')

# Cach 3: Binary Search
def binary_search(a, l, r, x) -> int:
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    q = int(input())
    for i in range(q):
        x = int(input())
        print('YES') if binary_search(a, 0, n - 1, x) != -1 else print('NO')
