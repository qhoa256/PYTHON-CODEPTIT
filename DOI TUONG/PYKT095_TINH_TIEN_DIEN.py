class KhachHang:
    def __init__(self, maKH, hoTen, loai, dau, cuoi):
        self.maKH = maKH
        self.hoTen = ' '.join(x.title() for x in hoTen.strip().split())
        self.loai = loai
        self.dau = dau
        self.cuoi = cuoi
        if self.loai == "A":
            self.dinhMuc = 100
        elif self.loai == "B":
            self.dinhMuc = 500
        else:
            self.dinhMuc = 200
        
        soDien = self.cuoi - self.dau
        if soDien < self.dinhMuc:
            self.tienDinhMuc = soDien * 450
            self.tienVuotDinhMuc = 0
            self.VAT = 0
        else:
            self.tienDinhMuc = self.dinhMuc * 450
            self.tienVuotDinhMuc = (soDien - self.dinhMuc) * 1000
            self.VAT = self.tienVuotDinhMuc // 20
        self.tongTien = self.tienDinhMuc + self.tienVuotDinhMuc + self.VAT
    def getTien(self):
        return self.tongTien
    def __str__(self):
        return f"{self.maKH} {self.hoTen} {self.tienDinhMuc} {self.tienVuotDinhMuc} {self.VAT} {self.tongTien}"
    
if __name__ == "__main__":
    res = []
    t = int(input())
    for i in range(1, t + 1):
        id = "KH" + format(i, '02d')
        hoTen = input()
        a = list(input().split())
        res.append(KhachHang(id, hoTen, a[0], int(a[1]), int(a[2])))
    res.sort(key = lambda x: -x.tongTien)
    for x in res:
        print(x)
