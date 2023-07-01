from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        cnt = 0
        for i in range(n):
            if gcd(i, n) == 1:
                cnt += 1
        if prime(cnt):
            print("YES")
        else:
            print("NO")

