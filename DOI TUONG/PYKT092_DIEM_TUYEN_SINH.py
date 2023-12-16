class ThiSinh:
  def __init__(self, id, hoTen, diem, danToc, khuVuc):
      self.id = "TS" + format(id, '02d')
      self.diem = diem + self.uuTienDT(danToc) + self.uuTienKV(khuVuc)
      self.hoTen = self.chuanHoa(hoTen)
      self.trangThai = 'Do' if self.diem >= 20.5 else 'Truot'
  def chuanHoa(self, hoTen):
      return ' '.join(i.capitalize() for i in hoTen.strip().split())
  def uuTienDT(self, danToc):
      if danToc == 'Kinh':
          return 0
      else:
          return 1.5
  def uuTienKV(self, khuVuc):
      if khuVuc == '1': return 1.5
      if khuVuc == '2': return 1
      return 0
  def __str__(self):
      return '{:s} {:s} {:.1f} {:s}'.format(self.id, self.hoTen, self.diem, self.trangThai)

if __name__ == '__main__':
    list = []
    t = int(input())
    for i in range(t):
      list.append(ThiSinh(i+1, input(), float(input()), input(), input()))
    list.sort(key = lambda x: (-x.diem, x.id));
    for x in list:
        print(x)