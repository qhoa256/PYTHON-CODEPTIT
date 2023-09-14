from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        n = int(s[-4::])
        if prime(n):
            print('YES')
        else:
            print('NO')
