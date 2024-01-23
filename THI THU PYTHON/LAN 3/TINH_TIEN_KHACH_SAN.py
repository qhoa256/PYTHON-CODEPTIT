from datetime import datetime
class KhachHang:
    def __init__(self, maKH, hoTen, soPhong, ngayNhan, ngayTra, dichVu):
        self.maKh = maKH
        self.hoTen = hoTen
        self.soPhong = soPhong
        date_format = "%d/%m/%Y"
        begin = datetime.strptime(ngayNhan, date_format)
        end = datetime.strptime(ngayTra, date_format)
        self.soNgay = (end - begin).days + 1
        self.dichVu = dichVu
    def tienPhong(self):
        x = self.soPhong[0]
        if x == '1':
            return 30
        elif x == '2':
            return 45
        elif x == '3':
            return 50
        elif x == '4':
            return 65
        elif x == '5':
            return 72
        elif x == '6':
            return 85
        elif x == '7':
            return 90
        elif x == '8':
            return 120
        elif x == '9':
            return 150
    def tongTien(self):
        return self.soNgay * self.tienPhong() + self.dichVu

    def __str__(self):
        return f"{self.maKh} {self.hoTen} {self.soPhong} {self.soNgay} {self.tongTien()}"
if __name__ == '__main__':
    t = int(input())
    kh = []
    for i in range(1, t + 1):
        maKH = "KH" + format(i, '02d')
        kh.append(KhachHang(maKH, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
    kh.sort(key = lambda x: (-x.tongTien(), x.soNgay))
    for x in kh:
        print(x)