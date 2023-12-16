import math
def prime(n):
  if n < 2:
    return False
  for i in range(2, math.isqrt(n) + 1):
    if n % i == 0:
      return False
  return True
if __name__ == "__main__":
  n = int(input())
  a = list(map(int, input().split()))
  P = sorted([i for i in a if prime(i)])
  idx = 0
  for x in a:
    if not x in P:
      print(x, end = ' ')
    else:
      print(P[idx], end = ' ')
      idx += 1