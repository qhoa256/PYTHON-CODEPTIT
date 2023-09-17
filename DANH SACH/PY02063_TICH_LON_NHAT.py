if __name__ == "__main__":
  n = int(input())
  a = list(map(int, input().split()))
  a.sort()
  x = a[0] * a[1]
  y = a[0] * a[1] * a[-1]
  z = a[-1] * a[-2]
  t = a[-1] * a[-2] * a[-3]
  print(max(x, y, z, t))