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
        if i % 2 == 0:
            if int(s[i]) % 2 != 0:
                return False
        if i % 2 != 0:
            if int(s[i]) % 2 == 0:
                return False
    return True

def sumDigit(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n
if __name__ == "__main__":
    t = int(input())
