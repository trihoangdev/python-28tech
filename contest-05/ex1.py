def do_something(a, n):
    dem_chan, dem_le, tong_chan, tong_le = 0, 0, 0, 0
    for x in a:
        if x % 2 == 0:
            dem_chan += 1
            tong_chan += x
        else:
            dem_le += 1
            tong_le += x
    print(dem_chan, dem_le, tong_chan, tong_le, sep='\n')


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    do_something(a, n)
