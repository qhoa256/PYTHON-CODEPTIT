from math import *

def prime(n):
  if n < 2:
    return False
  for i in range(2, isqrt(n) + 1):
    if n % i == 0:
      return False
  return True

if __name__ == "__main__":
  dict = ({})
  n = int(input())
  a = list(map(int, input().split()))
  for x in a:
    if prime(x):
      if x in dict:
        dict[x] += 1
      else:
        dict[x] = 1
  for val, fre in dict.items():
    print(val, fre)