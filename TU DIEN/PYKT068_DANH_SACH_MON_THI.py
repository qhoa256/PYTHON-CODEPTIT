class MonThi:
    def __init__(self, maMon, tenMon, hinhThuc):
        self.maMon = maMon
        self.tenMon = tenMon
        self.hinhThuc = hinhThuc
    def __str__(self):
        return f'{self.maMon} {self.tenMon} {self.hinhThuc}'
if __name__ == '__main__':
    t = int(input())
    mt = []
    while t > 0:
        t -= 1
        mt.append(MonThi(input().strip(), input().strip(), input().strip()))
    mt.sort(key = lambda x: x.maMon)
    for x in mt:
        print(x)

# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen
