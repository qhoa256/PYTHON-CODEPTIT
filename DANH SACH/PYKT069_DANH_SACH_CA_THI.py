class CaThi:
    def __init__(self, maCaThi, ngayThi, gioThi, phongThi):
        self.maCaThi = maCaThi
        self.ngayThi = ngayThi.strip()
        self.gioThi = gioThi.strip()
        self.phongThi = phongThi.strip()
        a = list(map(int, self.ngayThi.split("/")))
        b = list(map(int, self.gioThi.split(":")))
        self.ngay = a[0]
        self.thang = a[1]
        self.nam = a[2]
        self.gio = b[0]
        self.phut = b[1]

    def __str__(self):
        return f'{self.maCaThi} {self.ngayThi} {self.gioThi} {self.phongThi}'

if __name__ == "__main__":
    file = open('CATHI.in', 'r')
    n = int(file.readline())
    ct = [] 
    for i in range(n):
        maCaThi = "C" + format(i + 1, '03d')
        tmp = CaThi(maCaThi, file.readline(), file.readline(), file.readline())
        ct.append(tmp)
    ct.sort(key=lambda x: (x.nam, x.thang, x.ngay, x.gio, x.phut))
    for x in ct:
        print(x)