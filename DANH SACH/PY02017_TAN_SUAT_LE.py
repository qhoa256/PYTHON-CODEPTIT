if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for x in a:
      if x in d:
        d[x] += 1
      else:
        d[x]=1
    for x, y in d.items():
      if y % 2 == 1:
        print(x)
        break