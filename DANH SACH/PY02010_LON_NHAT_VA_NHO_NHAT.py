if __name__ == "__main__":
  i = 0
  while 1:
    n = int(input())
    if n == 0:
      break
    a = []
    for j in range(n):
      a.append(int(input()))
      i += 1
    if max(a) == min(a):
      print("BANG NHAU")
    else:
      print(min(a), max(a))
    a.clear()