if __name__ == "__main__":
  n = int(input())
  a = []
  for _ in range(n):
    x = list(map(int, input().split()))
    a.append(x)
  sum1, sum2 = 0, 0
  for i in range(n):
    for j in range(n):
      if j < i:
        sum1 += a[i][j]
      elif j > i:
        sum2 += a[i][j]
  k = int(input())
  if abs(sum2 - sum1) <= k:
    print("YES")
  else:
    print("NO")
  print(abs(sum1 - sum2))