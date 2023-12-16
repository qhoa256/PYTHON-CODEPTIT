if __name__ == "__main__":
  n = int(input())
  for _ in range(n):
    a = list(map(str, input().split()))
    res = 0
    for x in a:
      if res + len(x) <= 100:
        if res + len(x) < 100:
          print(x, end = ' ')
          res += len(x) + 1
        else:
          print(x, end = '')
          break
      else:
        break
    print()