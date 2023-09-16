def hexa(n):
  cnt = 0
  res = 0
  for i in range(len(n) - 1, -1, -1):
    if n[i] != '0':
      res += 2 ** cnt
    cnt += 1
  return str(res)
if __name__ == "__main__":
  n = input()
  while len(n) % 3 != 0:
    n = "0" + n
  res = ""
  for i in range(0, len(n), 3):
    res += hexa(n[i : i + 3])
  print(res)