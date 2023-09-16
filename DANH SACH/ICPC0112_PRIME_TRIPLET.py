from math import *

p = 1000001

prime = [1] * p

def sieve():
  prime[0], prime[1] = 0, 0
  for i in range(isqrt(p)):
    if prime[i]:
      for j in range(i * i, p, i):
        prime[j] = 0

if __name__ == '__main__':
  sieve()
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    res = 0
    for i in range(n - 4):
      if (prime[i] and prime[i + 2] and prime[i + 6]) or (prime[i] and prime[i + 4] and prime[i + 6]):
        res += 1
    print(res)