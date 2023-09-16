res = []

def init():
    queue = ['1','2']
    cnt = 0
    while cnt < 1001:
      k = str(queue.pop(0))
      if 2 * k.count('2') > len(k):
        cnt += 1
        res.append(k)
      queue.append(k+'0')
      queue.append(k+'1')
      queue.append(k+'2')

init()

if __name__ == '__main__':
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    for i in range(n):
      print(res[i], end = ' ')
    print()
