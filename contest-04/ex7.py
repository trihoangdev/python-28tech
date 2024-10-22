from math import factorial


def to_hop(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(to_hop(n,k))