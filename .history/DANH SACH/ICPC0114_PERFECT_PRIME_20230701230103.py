from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def primeDigits(n):
    sum = 0
    while n != 0:
        tmp = n % 10
        if tmp != 2 and tmp != 3 and tmp != 5 and tmp != 7:
            return False
        sum += tmp
        n //= 10
    return prime(sum)

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = input()
        r = n[: : -1]
        if
