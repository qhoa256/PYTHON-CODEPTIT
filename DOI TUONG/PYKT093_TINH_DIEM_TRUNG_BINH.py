from math import *

class SinhVien:
  def __init__(self, id, hoTen, mon1, mon2, mon3):
    self.id = "SV" + format(id, '02d')
    self.hoTen = self.chuanHoa(hoTen)
    self.diemTB = (mon1 * 3 + mon2 * 3 + mon3 * 2) / (3 + 3 + 2)

  def chuanHoa(self, hoTen):
    return ' '.join(i.title() for i in hoTen.strip().split())
  
  def __str__(self):
    return '{:s} {:s} {:.2f} {:d}'.format(self.id, self.hoTen, ceil(self.diemTB * 100) / 100, self.xepHang)

if __name__ == '__main__':
  sv = []
  n = int(input())
  for i in range(n):
    sv.append(SinhVien(i + 1, input(), float(input()), float(input()), float(input())))
  sv.sort(key = lambda x: (-x.diemTB, x.id))
  sv[0].xepHang = 1
  for i in range(1, len(sv)):
    if sv[i].diemTB == sv[i - 1].diemTB:
      sv[i].xepHang = sv[i - 1].xepHang
    else:
      sv[i].xepHang = i + 1
  print(*sv, sep = '\n')