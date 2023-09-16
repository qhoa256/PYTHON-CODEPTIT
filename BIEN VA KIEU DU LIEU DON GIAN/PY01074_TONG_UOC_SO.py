from math import *

minPrime = [0] * 2000001

def sieve():
    for i in range(2, isqrt(2000001)):
        if minPrime[i] == 0:
            for j in range(i * i, 2000001, i):
                if minPrime[j] == 0:
                    minPrime[j] = i
    for i in range(2, 2000001):
        if minPrime[i] == 0:
            minPrime[i] = i
def Ptich(n):
    res = 0
    while n != 1:
        res += minPrime[n]
        n //= minPrime[n]
    return res

if __name__ == "__main__":
    sieve()
    n = int(input())
    res = 0
    for i in range(n):
        x = int(input())
        res += Ptich(x)
    print(res)
