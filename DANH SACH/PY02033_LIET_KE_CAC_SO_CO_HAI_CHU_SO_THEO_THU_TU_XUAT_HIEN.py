if __name__ == "__main__":
  n = input()
  a = []
  end = (len(n) // 2) * 2
  i = 0
  cnt = [0] * 1005
  while i <= end - 2:
    x = int(n[i] + n[i + 1])
    cnt[x] += 1
    a.append(x)
    i += 2
  for x in a:
    if cnt[x] != 0:
      print(x, end = ' ')
      cnt[x] = 0