class CaThi:
    def __init__(self, maCaThi, ngay, gio, phong):
        self.maCaThi = maCaThi
        self.ngay = ngay
        self.gio = gio
        self.phong = phong

class LichThi:
    def __init__(self, maCaThi, ngay, gio, phong, mon, nhom, soLuong):
        self.maCaThi = maCaThi
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.mon = mon
        self.nhom = nhom
        self.soLuong = soLuong
    def getNgay(self):
        x = list(self.ngay.split('/'))
        return x[2] + x[1] + x[0]
    def __str__(self):
        return f"{self.ngay} {self.gio} {self.phong} {self.mon} {self.nhom} {self.soLuong}"
    
if __name__ == "__main__":
    f = open('MONTHI.in', 'r')
    n = int(f.readline().strip())
    d = dict()
    while n > 0:
        n -= 1
        a, b, c = f.readline().strip(), f.readline().strip(), f.readline().strip()
        d[a] = b
    f.close()
    f = open('CATHI.in', 'r')
    m = int(f.readline().strip())
    ct = []
    for i in range(1, m + 1):
        maCaThi = 'C' + format(i, '03d')
        x = CaThi(maCaThi, f.readline().strip(), f.readline().strip(), f.readline().strip())
        ct.append(x)
    f.close()
    f = open('LICHTHI.in', 'r')
    k = int(f.readline().strip())
    lt = []
    for i in range(k):
        x = list(map(str, f.readline().split()))
        maCaThi = x[0]
        maMon = x[1]
        nhom = x[2]
        soLuong = int(x[3])
        for h in ct:
            if h.maCaThi == maCaThi:
                lt.append(LichThi(maCaThi, h.ngay, h.gio, h.phong, d[maMon], nhom, soLuong))
                break
    lt.sort(key = lambda x: (x.getNgay(), x.gio, x.maCaThi))
    for x in lt:
        print(x)
    