from math import *
class HoaDon:
  def __init__(self, id, hoTen, dau, cuoi):
    self.id = "KH" + format(id, '02d')
    self.hoTen = hoTen
    self.dau = dau
    self.cuoi = cuoi
  def tongTien(self):
    x = self.cuoi - self.dau
    if x <= 50:
      return round(x * 100 * 102.0 / 100)
    elif 51 <= x <= 100:
      tmp1 = 50 * 100 + (x - 50) * 150
      return round(tmp1 * 103.0 / 100)
    else:
      tmp2 = 50 * 250 + (x - 100) * 200
      return round(tmp2 * 105.0 / 100) 
  def __str__(self):
      return f"{self.id} {self.hoTen} {self.tongTien()}"
 
if __name__ == "__main__":
  n = int(input())
  a = []
  for i in range(n):
    hoTen = input()
    dau = int(input())
    cuoi = int(input())
    a.append(HoaDon(i + 1, hoTen, dau, cuoi))
  a.sort(key = lambda x: - x.tongTien())
  for x in a: 
    print(x)