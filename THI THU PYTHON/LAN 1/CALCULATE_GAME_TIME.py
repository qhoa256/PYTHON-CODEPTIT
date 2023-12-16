class GameThu:
    def __init__(self, username, password, hoTen, gioVao, gioRa):
        self.username = username
        self.password = password
        self.hoTen = hoTen
        self.gioVao = gioVao
        self.gioRa = gioRa
        self.gio = 0
        self.phut = 0
    def thoiGian(self):
        x = list(self.gioVao.split(':'))
        y = list(self.gioRa.split(':'))
        sum = int(y[0]) * 60 + int(y[1]) - int(x[0]) * 60 - int(x[1])
        gio = sum // 60
        phut = sum - gio * 60
        self.gio = gio
        self.phut = phut
        return sum
    def __str__(self):
        return f"{self.username} {self.password} {self.hoTen} {self.gio} gio {self.phut} phut"
if __name__ == "__main__":
    n = int(input())
    gt = []
    while n > 0:
        n -= 1
        gt.append(GameThu(input().strip(), input().strip(), input().strip(), input().strip(), input().strip()))
    gt.sort(key = lambda x: (-x.thoiGian(), x.username))
    for x in gt:
        print(x)