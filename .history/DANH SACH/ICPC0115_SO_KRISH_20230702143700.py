from math import *

def sumDigits(n):
    sum = 0
    while n != 0:
        sum += factorial(n % 10)
        n //= 10
    return sum

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        if n == sumDigits(n):
            print()
