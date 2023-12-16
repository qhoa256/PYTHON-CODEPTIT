if __name__ == "__main__":
  n = input()
  k = int(input())
  d = dict()
  a = []
  end = (len(n) // 2) * 2
  i = 0
  while i <= end - 2:
    x = int(n[i] + n[i + 1])
    a.append(x)
    if x in d:
      d[x] += 1
    else:
      d[x] = 1
    i += 2
  a.sort()
  ok = 0
  for x in a:
    if d[x] >= k:
      print(x, d[x])
      d[x] = 0
      ok = 1
  if ok == 0:
    print("NOT FOUND")