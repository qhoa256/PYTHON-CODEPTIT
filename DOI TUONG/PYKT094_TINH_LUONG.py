d = dict()

class NhanVien:
    def __init__(self, maNV, hoTen, luongCB, soNgay):
        self.maNV = maNV
        self.hoTen = hoTen
        self.luongCB = luongCB
        self.soNgay = soNgay
        nhom = self.maNV[0]
        nam = int(self.maNV[1:3:])
        if 1 <= nam <= 3:
            if nhom == 'A' or nhom == 'B':
                self.heSo = 10
            elif nhom == 'C':
                self.heSo = 9
            else:
                self.heSo = 8
        elif 4 <= nam <= 8:
            if nhom == 'A':
                self.heSo = 12
            elif nhom == 'B':
                self.heSo = 11
            elif nhom == 'C':
                self.heSo = 10
            else:
                self.heSo = 9
        elif 9 <= nam <= 15:
            if nhom == 'A':
                self.heSo = 14
            elif nhom == 'B':
                self.heSo = 13
            elif nhom == 'C':
                self.heSo = 12
            else:
                self.heSo = 11
        else:
            if nhom == 'A':
                self.heSo = 20
            elif nhom == 'B':
                self.heSo = 16
            elif nhom == 'C':
                self.heSo = 14
            else:
                self.heSo = 13
        self.tongLuong = self.luongCB * self.soNgay * self.heSo * 1000
    def __str__(self):
        return f"{self.maNV} {self.hoTen} {d[self.maNV[3:]]} {self.tongLuong}"


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = list(input().split())
        b = a[1:]
        d[a[0]] = ' '.join(b)
    m = int(input())
    res = []
    for _ in range(m):
        res.append(NhanVien(input(), input(), int(input()), int(input())))
    for x in res:
        print(x)
