class Matrix:
  def __init__(self, n, m, mt):
    self.n = n
    self.m = m
    self.mt = mt
  def mul_transpose(self):
    res = []
    for i in range(self.n):
      res += [[0] * self.n]
    for i in range(self.n):
      for j in range(self.n):
        for k in range(self.m):
          res[i][j] += self.mt[i][k] * self.mt[j][k]
    return Matrix(self.n, self.m, res)
  def __str__(self):
    for i in self.mt:
      print(*i)
    return ''
if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n, m = map(int, input().split())
    list = []
    for i in range(n):
      list.append([int(j) for j in input().split()])
    x = Matrix(n, m, list)
    print(x.mul_transpose())
