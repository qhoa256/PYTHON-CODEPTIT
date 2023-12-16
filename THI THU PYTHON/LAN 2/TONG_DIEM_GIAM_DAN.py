class ThiSinh:
    def __init__(self, stt, hoTen, ngaySinh, diem1, diem2, diem3):
        self.stt = stt
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.tongDiem = diem1 + diem2 + diem3
    def __str__(self):
        return f"{self.stt} {self.hoTen} {self.ngaySinh} {self.tongDiem:.1f}"
if __name__ == '__main__':
    t = int(input())
    ts = []
    for i in range(1, t + 1):
        ts.append(ThiSinh(i, input().strip(), input().strip(), float(input().strip()), float(input().strip()), float(input().strip())))
    ts.sort(key = lambda x: (-x.tongDiem, x.stt))
    for x in ts:
        print(x)
