def so_loc_phat(n):
    while n != 0:
        temp = n % 10
        if temp != 0 and temp != 6 and temp != 8:
            return False
        n //= 10
    return True


if __name__ == '__main__':
    n = int(input())
    print(1) if so_loc_phat(n) else print(0)
