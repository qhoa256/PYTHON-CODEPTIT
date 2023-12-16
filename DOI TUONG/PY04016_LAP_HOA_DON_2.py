from datetime import datetime

class HoaDon:
  def __init__(self, id, hoTen, soPhong, ngayNhan, ngayTra, dichVu):
    self.id = "KH" + format(id, '02d')
    self.hoTen = hoTen
    self.soPhong = soPhong
    self.ngayNhan = ngayNhan
    self.ngayTra = ngayTra
    self.dichVu = dichVu
    date_format = "%d/%m/%Y"
    begin = datetime.strptime(self.ngayNhan, date_format)
    end = datetime.strptime(self.ngayTra, date_format)
    time = end - begin
    self.soNgay = time.days + 1
  def tongTien(self):
    if self.soPhong[0] == '1':
        return 25 * self.soNgay + self.dichVu
    elif self.soPhong[0] == '2':
        return 34 * self.soNgay + self.dichVu
    elif self.soPhong[0] == '3':
        return 50 * self.soNgay + self.dichVu
    else:
        return 80 * self.soNgay + self.dichVu
  def __str__(self):
    return "{} {} {} {} {}".format(self.id, self.hoTen, self.soPhong, self.soNgay, self.tongTien())
    
if __name__ == "__main__":
  n = int(input())
  res = []
  for i in range(n):
    res.append(HoaDon(i + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
  res.sort(key = lambda x : -x.tongTien())
  for x in res:
    print(x)