class gameThu:
  def __init__(self, id, hoTen, gioVao, gioRa):
    self.id = id
    self.hoTen = hoTen
    self.gioVao = gioVao
    self.gioRa = gioRa
  def soPhut(self):
    x = int(self.gioVao[:2]) * 60 + int(self.gioVao[3:])
    y = int(self.gioRa[:2]) * 60 + int(self.gioRa[3:])
    return y - x
  def __str__(self):
    tong = self.soPhut()
    gio = tong // 60
    phut = tong - gio * 60
    return f'{self.id} {self.hoTen} {gio} gio {phut} phut'

if __name__ == '__main__':
  t = int(input())
  a = []
  while t > 0:
    t -= 1
    a.append(gameThu(input(), input(), input(), input()))
  a.sort(key = lambda x: -x.soPhut())
  for x in a:
    print(x)