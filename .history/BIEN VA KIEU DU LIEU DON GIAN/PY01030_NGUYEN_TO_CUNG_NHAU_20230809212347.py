from math import *

if __name__ == '__main__':
    n, k = map(int, input().split())
    cnt = 0
    for i in range(pow(10, k - 1), pow(10, k)):
        if gcd(n, i) == 1:
            cnt += 1
            print(i, end = ' ')