if __name__ == "__main__":
  n = int(input())
  a = []
  for _ in range(n):
    a.append(input())
  i = 0
  res = []
  while i < n - 1:
    if len(list(map(str, a[i].split()))) == 7:
      res.append(2)
      i += 4
    else:
      res.append(1)
      while len(list(map(str, a[i].split()))) != 7 and i < n - 1:
        i += 1
  print(len(res))
  for x in res:
    print(x)
  
