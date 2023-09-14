if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n = input()
    if len(n) < 3:
      print("NO")
    else:
      tmp = n[0]
      i = 1
      while ord(tmp) < ord(n[i]):
        tmp = n[i]
        i += 1
      ok = 1
      for j in range(i + 1, len(n)):
        if ord(n[j]) > ord(n[j - 1]):
          ok = 0
          break
      if ok:
        print("YES")
      else:
        print("NO")