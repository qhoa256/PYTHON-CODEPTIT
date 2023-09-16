from collections import Counter

if __name__ == '__main__':
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    check = 0
    for c in Counter(a).items():
      if c[1] > n / 2:
          check = 1
          print(c[0])
    if check == 0:
        print("NO")