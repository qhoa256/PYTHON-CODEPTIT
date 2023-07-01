from math import *

def Ptich(n):
    sum = 0
    for i in range(2, isqrt(n) + 1):
        while n % i == 0:
            sum += i
            n //= i
    if n != 1:
        sum += n
    return sum

if __name__ == "__main__":
    n = int(input())
    res = 0
    for i in range(n):
        x = int(input())
