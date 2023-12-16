class SoPhuc:
  def __init__(self, thuc, ao):
    self.thuc, self.ao = thuc, ao
  
  def __add__(self, p):
    return SoPhuc(self.thuc + p.thuc, self.ao + p.ao)
  
  def __mul__(self, p):
    return SoPhuc(self.thuc * p.thuc - self.ao * p.ao, self.thuc * p.ao + self.ao * p.thuc)
  
  def __pow__(self, o):
    res = self
    while o > 1:
      o -= 1
      res = res * self
    return res
  
  def __str__(self):
    dau = '+'
    if self.ao < 0:
      dau = '-'
    return f"{self.thuc} {dau} {abs(self.ao)}i"

if __name__ == '__main__':
  test = int(input())
  while test > 0:
    test -= 1
    a = list(map(int, input().split()))
    x = SoPhuc(a[0], a[1])
    y = SoPhuc(a[2], a[3])
    z = (x + y) * x
    t = (x + y) ** 2
    print(f"{z}, {t}")