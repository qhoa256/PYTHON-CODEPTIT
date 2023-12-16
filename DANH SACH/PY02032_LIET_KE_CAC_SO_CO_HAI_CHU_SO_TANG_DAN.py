if __name__ == "__main__":
  n = input()
  a = []
  end = (len(n) // 2) * 2
  i = 0
  while i <= end - 2:
    a.append(int(n[i] + n[i + 1]))
    i += 2
  A = set(a)
  for x in sorted(list(A)):
    print(x, end = ' ')