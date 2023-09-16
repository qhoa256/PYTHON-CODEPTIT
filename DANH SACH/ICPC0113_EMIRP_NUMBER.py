from math import *

p = 1000001
prime = [1] * p

def sieve():
  prime[0], prime[1] = 0, 0
  for i in range(isqrt(p)):
    if prime[i]:
      for j in range(i * i, p, i):
        prime[j] = 0

if __name__ == "__main__":
  sieve()
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    dic = {}
    for i in range(13, n):
        num = int(str(i)[::-1])
        if prime[i] == 0 or prime[num] == 0 or num >= n or num in dic or i == num:
            continue
        print(i, num, end = " ")
        dic[num] = dic[i] = 1
    print()
    