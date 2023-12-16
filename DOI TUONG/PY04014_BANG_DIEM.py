def custom_round(number, decimal_places):
  factor = 10 ** decimal_places
  rounded_number = int(number * factor + 0.5) / factor
  return rounded_number
class bangDiem:
  def __init__(self, id, name, toan, van, anh, ly, hoa, sinh, su, dia, gdcd, cn):
    self.id = "HS" + format(id, '02d')
    self.name = name
    self.toan = toan
    self.van = van
    self.anh = anh
    self.ly = ly
    self.hoa = hoa
    self.sinh = sinh
    self.su = su
    self.dia = dia
    self.gdcd = gdcd
    self.cn = cn
  def diemTB(self):
    return custom_round((self.toan * 2 + self.van * 2 + self.anh + self.ly + self.hoa + self.sinh + self.su + self.dia + self.gdcd + self.cn) / 12, 1)
  def xepLoai(self):
    dtb = self.diemTB()
    if dtb >= 9.0:
      return ('XUAT SAC')
    elif dtb >= 8.0:
      return ('GIOI')
    elif dtb >= 7.0:
      return ('KHA')
    elif dtb >= 5.0:
      return ('TB')
    else:
      return ('YEU')
  def __str__(self):
    return f'{self.id} {self.name} {self.diemTB():.1f} {self.xepLoai()}'
if __name__ == "__main__":
  t = int(input())
  a = []
  for i in range(1, t + 1):
    s = input()
    b = list(map(float, input().split()))
    a.append(bangDiem(i, s, b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9]))
  a.sort(key = lambda x: -x.diemTB())
  for x in a:
    print(x)

