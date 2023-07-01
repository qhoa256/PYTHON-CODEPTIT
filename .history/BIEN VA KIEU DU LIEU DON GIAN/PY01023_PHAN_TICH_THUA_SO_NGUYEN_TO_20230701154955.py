from math import *

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        print('1 * ', end = '')
        for i in range(2, isqrt(n) + 1):
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            if cnt != 0:
                print(i, cnt, sep = '^', end = '')
                if n != 1:
                    print(' * ', end = '')
        if n != 1:
            print(n, 1, sep = '^', end = '\n')
        t -= 1  
