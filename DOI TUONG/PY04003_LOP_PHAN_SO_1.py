from math import *

class PhanSo:
  def __init__(self, tu, mau):
    self.tu = tu
    self.mau = mau
  def rutgon(self):
    mc = gcd(self.tu, self.mau)
    self.tu = self.tu // mc
    self.mau = self.mau // mc
  def __str__(self):
      return "{}/{}".format(self.tu, self.mau)
if __name__ == "__main__":
  a, b = map(int, input().split())
  x = PhanSo(a, b)
  x.rutgon()
  print(x)