def convolution():
  u = n - 2
  v = m -2
  res = 0
  for i in range(u):
    for j in range(v):
      res += sum([sum([x[i1 + i][i2 + j] * h[i1][i2] for i2 in range(3)]) for i1 in range(3)])
  return res
if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n, m = map(int, input().split())
    x = [list(map(int, input().split())) for i in range(n)]
    h = [list(map(int, input().split())) for i in range(3)]          
    print(convolution())