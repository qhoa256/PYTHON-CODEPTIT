def check(a, b, n):
  for i in range(n):
    if a[i] > b[i]:
      return False
  return True
if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    if check(a, b, n):
      print("YES")
    else:
      print("NO")