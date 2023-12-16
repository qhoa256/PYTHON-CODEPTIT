class SinhVien:
    def __init__(self, hoTen, accepted, submit):
        self.hoTen = hoTen
        self.accepted = accepted
        self.submit = submit
    def __str__(self):
        return f"{self.hoTen} {self.accepted} {self.submit}"

if __name__ == '__main__':
    t = int(input())
    sv = []
    while t > 0:
        t -= 1
        hoTen = input()
        a, s = map(int, input().split())
        sv.append(SinhVien(hoTen, a, s))
    sv.sort(key = lambda x: (-x.accepted, x.submit, x.hoTen))
    for x in sv:
        print(x)
