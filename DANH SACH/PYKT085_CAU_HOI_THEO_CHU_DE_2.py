if __name__ == "__main__":
  t = int(input())
  a = []
  while t > 0:
    t -= 1
    s = input()
    a.append(s)
    if s == "": 
      print(a[0] + ": " + str(len(a) - 2))
      a.clear()
  print(a[0] + ": " + str(len(a) - 1))