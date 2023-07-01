from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    s = str(n)
    for i in range(len(s)):
        if i % 2 ==

if __name__ == "__main__":
    t = int(input())
