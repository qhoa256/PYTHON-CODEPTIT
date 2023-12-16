from datetime import datetime

class MonHoc:
  def __init__(self, maMon, tenMon):
    self.maMon = maMon
    self.tenMon = tenMon
  def __str__(self):
    return f"{self.maMon} {self.tenMon}"

stt = 1

class LichThi:
  def __init__(self, ngay, gio, nhom, monHoc):
    self.thoiGian = ' '.join([ngay, gio])
    self.nhom = nhom
    self.monHoc = monHoc
    global stt
    self.ma = "T" + format(stt, '03d')
    stt += 1
  
  def __lt__(self, x):
    n1 = datetime.strptime(self.thoiGian, "%d/%m/%Y %H:%M")
    n2 = datetime.strptime(x.thoiGian, "%d/%m/%Y %H:%M")
    if n1 == n2:
      return str(self.monHoc) < str(x.monHoc)
    return n1 < n2
  
  def __str__(self):
    return "{} {} {} {} ".format(self.ma, self.monHoc, self.thoiGian, self.nhom)
  
if __name__ == '__main__':
  n, m = map(int, input().split())
  mh = []
  lt = []
  for i in range(n):
    mh.append(MonHoc(input(), input()))
  for i in range(m):
    maMon, ngay, gio, nhom = input().split()
    for j in mh:
      if j.maMon == maMon:
        lt.append(LichThi(ngay, gio, nhom, j))
  lt.sort()
  for x in lt:
    print(x)