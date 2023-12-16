from math import *

def BCNN(a, b):
    return a // gcd(a, b) * b

class PhanSo:
  def __init__(self, tu, mau):
    self.tu = tu
    self.mau = mau
  def rutgon(self):
    mc = gcd(self.tu, self.mau)
    self.tu = self.tu // mc
    self.mau = self.mau // mc
  def tong(self, a):
    self.rutgon()
    a.rutgon()
    y = BCNN(a.mau, self.mau)
    x = y //a.mau * a.tu + y // self.mau * self.tu 
    res = PhanSo(x, y)
    res.rutgon()
    return res
  def __str__(self):
    return "{}/{}".format(self.tu, self.mau)
if __name__ == "__main__":
  a, b, c, d = map(int, input().split())
  x = PhanSo(a, b)
  y = PhanSo(c, d)
  print(x.tong(y))