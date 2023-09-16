if __name__ == "__main__":
  n = int(input())
  a = list(map(float, input().split()))
  res = []
  for x in a:
    if x != min(a) and x != max(a):
      res.append(x)
  print('{:.2f}'.format(sum(res) / len(res)))