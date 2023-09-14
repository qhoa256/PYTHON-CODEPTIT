from math import *

if __name__ == "__main__":
  test = int(input())
  while test > 0:
    test -= 1
    s = input()
    t = s[: : -1]
    ok = 1
    for i in range(1, len(s)):
      if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(t[i]) - ord(t[i - 1])):
        ok = 0
        break
    if ok:
      print("YES")
    else:
      print("NO")
