from functools import cmp_to_key
def sum(n):
  res = 0
  for x in str(n):
    res += int(x)
  return res
def cmp(a, b):
  if sum(a) != sum(b): 
    return sum(a) - sum(b)
  elif a != b: 
    return a - b

if __name__ == '__main__':
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = cmp_to_key(cmp))
    for x in a:
      print(x, end = " ")
    print()