from functools import cmp_to_key
class CauThu:
    def __init__(self, maCT, hoTen, doiBong, ngaySinh, chieuCao, viTri):
        self.maCT = maCT
        self.hoTen = hoTen
        self.doiBong = doiBong
        if ngaySinh[1] == '/':
            ngaySinh = '0' + ngaySinh
        if ngaySinh[4] == '/':
            ngaySinh = ngaySinh[0:3] + '0' + ngaySinh[3:]
        self.ngaySinh = ngaySinh
        self.chieuCao = chieuCao
        self.viTri = viTri
    def tuoi(self):
        x = list(self.ngaySinh.split("/"))
        return int(x[2] + x[1] + x[0])
    def __str__(self):
        return f"{self.maCT} {self.hoTen} {self.doiBong} {self.ngaySinh} {self.chieuCao} {self.viTri}"

def cmp(a, b):
    if a.tuoi() < b.tuoi():
        return 1
    elif a.tuoi() > b.tuoi():
        return -1
    else:
        return a.chieuCao - b.chieuCao
if __name__ == "__main__":
    d = dict()
    t = int(input())
    ct = []
    while t > 0:
        t -= 1
        hoTen = input().strip()
        doiBong = input().strip()
        ngaySinh = input().strip()
        chieuCao = int(input().strip())
        viTri = input()
        tmp = list(viTri.split())
        qhoa = ""
        for x in tmp:
            qhoa += x[0]
        stt = 0
        if qhoa in d:
            d[qhoa] += 1
            stt = d[qhoa]
        else:
            d[qhoa] = 1
            stt = d[qhoa]
        maCT = qhoa + format(stt, '02d')
        q = CauThu(maCT, hoTen, doiBong, ngaySinh, chieuCao, viTri)
        ct.append(q)
    ct.sort(key = cmp_to_key(cmp))
    for x in ct:
        print(x)