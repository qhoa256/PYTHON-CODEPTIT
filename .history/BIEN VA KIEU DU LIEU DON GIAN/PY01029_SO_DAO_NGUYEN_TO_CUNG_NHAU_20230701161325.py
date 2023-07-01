from math import *

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        a = input()
        b = a[: : -1]
        if gcd(int(a), int(b)) == 1:
            print('YES')
        else:
            print('NO')
        