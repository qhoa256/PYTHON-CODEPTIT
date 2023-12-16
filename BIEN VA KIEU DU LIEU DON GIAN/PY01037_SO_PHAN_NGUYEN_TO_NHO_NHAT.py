from math import *

divisors = [0] * (10 ** 7 + 1)

def countDivisors(n):
    cnt = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            cnt += 1
            if i != (n // i):
                cnt += 1
    return cnt

def init():
    for i in range(1, 10 ** 7 + 1):
        divisors[i] = countDivisors(i)

def solve(n):
    for j in range(1, n):
        if divisors[n] <= divisors[j]:
            return False
    return True

if __name__ == "__main__":
    init()
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        for i in range(n, 10 ** 7 + 1):
            if solve(i):
                print(i)
                break