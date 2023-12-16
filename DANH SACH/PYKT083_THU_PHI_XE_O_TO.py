def money(a, b):
  if a == "Xe_con":
    if b == "5":
      return 10000
    else:
      return 15000
  elif a == "Xe_tai":
    return 20000
  else:
    if b == "29":
      return 50000
    else:
      return 70000
if __name__ == "__main__":
  n = int(input())
  d = dict()
  for i in range(n):
    a = list(map(str, input().split()))
    if a[4] in d:
      if a[3] == "IN":
        d[a[4]] += money(a[1], a[2])
    else:
      if a[3] == "IN":
        d[a[4]] = money(a[1], a[2])
  for x, y in d.items():
    print(f'{x}: {y}')
    