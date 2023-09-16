if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(d, n):
      print(a[i], end = ' ')
    for i in range(d):
      print(a[i], end = ' ')
    print()