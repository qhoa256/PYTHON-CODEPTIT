if __name__ == "__main__":
  n = int(input())
  sum = 0
  a = list(map(int, input().split()))
  for i in range(0, n - 1) :
      for j in range(i + 1, n) :
          if a[i] > a[j] : 
             sum += 1
  print(sum)