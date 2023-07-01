from math import *

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        print('1 * ')
        for i in range(2, isqrt(n) + 1):
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(i, cnt, sep = '^')   
