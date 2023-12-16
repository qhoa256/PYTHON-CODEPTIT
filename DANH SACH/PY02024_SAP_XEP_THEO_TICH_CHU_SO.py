from functools import cmp_to_key

def mul(n):
  res = 1
  for i in str(n):
    res *= int(i)
  return res

def cmp(a, b):
  if mul(a) != mul(b):
    return mul(a) - mul(b)
  else:
    return a - b
  
if __name__ == '__main__':
  t = int(input())
  while t > 0:
    t -= 1
    n = input()
    a = list(map(int, input().split()))
    a.sort(key = cmp_to_key(cmp))
    for i in a:
      print(i, end = ' ')
    print()