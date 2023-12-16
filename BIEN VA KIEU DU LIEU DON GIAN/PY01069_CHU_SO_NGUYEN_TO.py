def check(s):
  if int(s) % 2 == 0:
    return False
  cnt2, cnt3, cnt5, cnt7 = 0, 0, 0, 0
  for c in s:
    if c == '2':
        cnt2 += 1
    elif c == '3':
        cnt3 += 1
    elif c == '5':
        cnt5 += 1
    elif c == '7':
        cnt7 += 1
  return cnt2 > 0 and cnt3 > 0 and cnt5 > 0 and cnt7 > 0

def Try(s):
    if len(s) >= 4 and check(s):
      a.append(s)
    if len(s) < n:
      Try(s + '2')
      Try(s + '3')
      Try(s + '5')
      Try(s + '7')
if __name__ == '__main__':
  n = int(input())
  a = []
  Try('')
  a.sort(key=lambda x: (len(x), x))
  for x in a:
      print(x)
