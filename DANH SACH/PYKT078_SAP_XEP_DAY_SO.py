if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
      if a[i] == max(a):
        a.insert(i, m)
        break
    b, c = [], []
    for x in a:
      if x < 0:
        b.append(x)
      else:
        c.append(x)
    for x in b:
      print(x, end = ' ')
    for x in c:
      print(x, end = ' ')
    print()