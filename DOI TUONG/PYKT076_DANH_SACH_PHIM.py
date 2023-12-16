d = dict()
class Phim:
  def __init__(self, id, theLoai, ngayChieu, tenPhim, soTap):
      self.id = "P" + "{:03d}".format(id)
      self.theLoai = d[theLoai]
      self.ngayChieu = ngayChieu 
      self.tenPhim = tenPhim
      self.soTap = soTap
      a = list(map(int, self.ngayChieu.split("/")))
      self.ngay = int(a[0])
      self.thang = int(a[1])
      self.nam = int(a[2])
  def __str__ (self):
      return "{} {} {} {} {}".format(self.id, self.theLoai, self.ngayChieu, self.tenPhim, self.soTap)
      
if __name__ == "__main__":
  n, m = map(int, input().split())
  for i in range(n):
    s = "TL" + "{:03d}".format(i + 1)
    s1 = input().strip()
    d[s] = s1 
  a = []
  for i in range(0, m):
    tmp = Phim(i + 1, input(), input(), input(), (int(input().strip())))
    a.append(tmp) 
  a.sort(key = lambda x: (x.nam, x.thang, x.ngay, x.tenPhim, -x.soTap))
  for x in a: 
    print(x)