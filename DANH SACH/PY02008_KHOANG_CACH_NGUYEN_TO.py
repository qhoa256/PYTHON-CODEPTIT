import math

p = 10001
prime = [1] * p

def sieve():
  prime[0] = prime[1] = 0
  for i in range(math.isqrt(p)):
    if prime[i]:
      for j in range(i * i, p, i):
        prime[j] = 0

if __name__ == '__main__':
  sieve()
  list = []
  for i in range(p):
    if prime[i]:
      list.append(i)
  n, x = map(int, input().split())
  i = 0
  tmp = x
  while i <= n:
    print(tmp, end = ' ')
    tmp += list[i]
    i += 1
