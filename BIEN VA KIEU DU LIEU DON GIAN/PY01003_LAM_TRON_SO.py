if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    a = [int(i) for i in str(n)]
    for i in range(len(a) - 1, 0, -1):
      if a[i] >= 5:
        a[i - 1] += 1
      a[i] = 0
    print(int(''.join([str(i) for i in a])))
