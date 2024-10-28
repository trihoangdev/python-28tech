if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    y = int(input())
    larger_cnt, less_cnt = 0, 0
    for x in a:
        if x > y:
            larger_cnt += 1
        elif x < y:
            less_cnt += 1
    print(less_cnt, larger_cnt, sep='\n')
