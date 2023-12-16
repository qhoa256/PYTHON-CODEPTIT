class DanhBa:
    def __init__(self, hoTen, soDT, ngay):
        self.hoTen = hoTen
        self.soDT = soDT
        self.ngay = ngay.strip()
        a = list(self.hoTen.split())
        self.ten = a[-1]
        self.ho= a[0]
        self.dem =""
        for i in range(1, len(a) -1): 
            self.dem += a[i] + ' '
    def __str__ (self):
        return "{}: {} {}".format(self.hoTen, self.soDT, self.ngay[4::].strip())
if __name__ == '__main__':
    file = open("SOTAY.txt", 'r')
    a = []
    for line in file: 
        a.append(line.strip())
    b = []
    i = 0
    while(i < len(a)):
        if(a[i][:4:]=="Ngay"):
            s = a[i]
            tmp = i + 1
            while(a[tmp][:4:] != "Ngay"):
                tmp1 = DanhBa(a[tmp], a[tmp + 1], s)
                b.append(tmp1)
                tmp += 2 
                if(tmp >= len(a)): 
                    break
        i = tmp
    b.sort(key = lambda x: (x.ten, x.ho, x.dem))
    out = open("DIENTHOAI.txt", 'w')
    for i in b: out.write(i.__str__() + "\n")
    out.close()