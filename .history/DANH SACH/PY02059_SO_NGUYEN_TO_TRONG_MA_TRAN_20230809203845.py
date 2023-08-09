from math import *

prime = [True] * (1001)

def sieve():
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(1001) + 1):
        if prime[i]:
            for j in range(i * i, 1001, i)
if __name__ == "__main__":
