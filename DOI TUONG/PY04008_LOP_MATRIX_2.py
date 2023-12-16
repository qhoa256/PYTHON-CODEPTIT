class Matrix:
    def __init__(self, n , m, mt):
        self.n = n
        self.m = m
        self.mt = mt
    
    def solve(self):
        res = []
        for i in range(self.n):
            res += [[0] * self.n]
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    res[i][j] += self.mt[i][k] * self.mt[j][k]
        return Matrix(self.n, self.n, res)

    def __str__(self):
        for item in self.mt:
            print(*item)
        return "" 
if __name__ == "__main__":
    list, t, i = [], int(input()), 0
    try:
      while True:
          value = [int(i) for i in input().split()]
          list += value
    except EOFError:
      pass
    for k in range(t):
      n,m = list[i], list[i+1]
      i+=2
      tmp = []
      for _ in range(n):
          tmp.append(list[i:i+m])
          i += m
      mt = Matrix(n, m, tmp)
      print(mt.solve())