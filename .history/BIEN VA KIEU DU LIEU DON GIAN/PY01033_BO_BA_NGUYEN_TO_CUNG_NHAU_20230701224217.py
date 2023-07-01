from math import *

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b - 1):
        for j in range(i + 1, b):
            for k in range(j + 1, b + 1):
                if gcd(i, j) == 1 and gcd
