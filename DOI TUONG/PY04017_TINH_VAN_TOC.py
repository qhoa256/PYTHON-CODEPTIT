from datetime import datetime

class Cyclist:
  def __init__(self, name, place, time):
    self.name = name
    self.place = place
    self.id = ''.join(i[0] for i in place.split() + name.split())
    h , m = map(int, time.split(':'))
    self.V = 120 / (h + m/60 - 6)
  def __str__(self):
    return "{} {} {} {} Km/h".format(self.id, self.name, self.place, round(self.V))
  
if __name__ == '__main__':
  t = int(input())
  list = []
  while t > 0:
    t -= 1
    list.append(Cyclist(input(), input(), input()))
  list.sort(key = lambda x: -x.V)
  for x in list:
    print(x)