if __name__ == "__main__":
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  a.sort()
  b.sort()
  A = set(a)
  B = set(b)
  res1 = list(A.intersection(B))
  res1.sort()
  for x in res1:
    print(x, end = ' ')
  print()
  res2 = list(A.difference(B))
  res2.sort()
  for x in res2:
    print(x, end = ' ')
  print()
  res3 = list(B.difference(A))
  res3.sort()
  for x in res3:
    print(x, end = ' ')
  print()