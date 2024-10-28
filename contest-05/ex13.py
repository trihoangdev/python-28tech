if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    const = 10 ** 9 + 7
    tong, tich = 0, 1
    for i in range(n):
        tong += a[i]
        tong %= const
        tich *= a[i]
        tich %= const
    print(tong, tich, sep='\n')
