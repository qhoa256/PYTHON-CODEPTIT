class TramDo:
    def __init__(self, maTram, tenTram):
        self.maTram = maTram
        self.tenTram = tenTram
        self.luongMua = 0
        self.gioMua = 0.0
    def luongMuaTB(self):
        return self.luongMua / self.gioMua
    def __str__(self):
        return f"{self.maTram} {self.tenTram} {self.luongMuaTB():.2f}"
if __name__ == "__main__":
    S = set()
    n = int(input())
    id = 1
    res = []
    for _ in range(n):
        a = input()
        b = input()
        c = input()
        d = int(input())
        x = b.split(":")
        y = c.split(":")
        x1, x2, y1, y2 = int(x[0]), int(x[1]), int(y[0]), int(y[1])
        thoiGian = (y1 * 60 + y2 - x1 * 60 - x2) / 60.0
        if a not in S:
           maTram = "T" + format(id, '02d')
           object = TramDo(maTram, a)
           object.gioMua += thoiGian
           object.luongMua += d
           res.append(object)
           S.add(a)
           id += 1
        else:
            for i in range(len(res)):
                if res[i].tenTram == a:
                    res[i].luongMua += d
                    res[i].gioMua += thoiGian
                    break
    for x in res:
        print(x)

           
