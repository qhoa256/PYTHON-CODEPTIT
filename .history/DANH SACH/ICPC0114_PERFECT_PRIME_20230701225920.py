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
    while t != 0:
        n = input()
        r = n[: : -1]
