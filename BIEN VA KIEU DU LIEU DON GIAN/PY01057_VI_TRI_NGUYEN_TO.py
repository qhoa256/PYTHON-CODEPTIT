from math import *

prime = [True] * 1001

def sieve():
    prime[0], prime[1] = False, False
    for i in range(isqrt(1001)):
        if prime[i]:
            for j in range(i * i, 1001, i):
                prime[j] = False

def check(n):
    for i in range(len(n)):
        if prime[i] + prime[int(n[i])] == 1:
            return False
    return True

if __name__ == "__main__":
    sieve()
    t = int(input())
    while t != 0:
        n = input()
        if check(n):
            print('YES')
        else:
            print('NO')
        t -= 1