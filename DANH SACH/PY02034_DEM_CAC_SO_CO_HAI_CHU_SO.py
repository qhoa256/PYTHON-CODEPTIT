if __name__ == "__main__":
  n = input()
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
  for x in a:
    if d[x] != 0:
      print(x, d[x])
      d[x] = 0