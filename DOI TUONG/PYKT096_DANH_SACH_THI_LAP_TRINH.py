dMa = dict()
dTen = dict()

class ThiSinh:
    def __init__(self, maTS, hoTen, maNhom, tenNhom):
        self.maTS = maTS
        self.hoTen = hoTen
        self.maNhom = maNhom
        self.tenNhom = tenNhom
    def __str__(self):
        return f"{self.maTS} {self.hoTen} {self.maNhom} {self.tenNhom}"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        nhom = "Team" + format(i + 1, '02d')
        maNhom = input()
        tenNhom = input()
        dMa[nhom] = maNhom
        dTen[nhom] = tenNhom
    n = int(input())
    ts = []
    for i in range(1, n + 1):
        maTS = "C" + format(i, '03d')
        hoTen = input()
        nhom = input()
        ts.append(ThiSinh(maTS, hoTen, dMa[nhom], dTen[nhom]))
    ts.sort(key = lambda x: x.hoTen)
    for x in ts:
        print(x)
        

