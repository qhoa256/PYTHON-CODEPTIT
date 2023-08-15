from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        sum = 0
        for x in n:
            sum += int(x)
        if prime(sum):
            print("Y")