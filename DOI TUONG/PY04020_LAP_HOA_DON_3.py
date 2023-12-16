class hoaDon:
  def __init__(self, id, tenSP, soLuong, donGia, chietKhau):
    self.id = id
    self.tenSP = tenSP
    self.soLuong = soLuong
    self.donGia = donGia
    self.chietKhau = chietKhau
  def tongTien(self):
    return self.soLuong * self.donGia - self.chietKhau
  def __str__(self):
    return f'{self.id} {self.tenSP} {self.soLuong} {self.donGia} {self.chietKhau} {self.tongTien()}'

if __name__ == '__main__':
  t = int(input())
  a = []
  for _ in range(t):
    a.append(hoaDon(input(), input(), int(input()), int(input()), int(input())))
  a.sort(key = lambda x: -x.tongTien())
  for x in a:
    print(x)