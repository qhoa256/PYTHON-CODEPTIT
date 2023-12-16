if __name__ == "__main__":
  n = input()
  while len(n) > 1:
    x = len(n) // 2
    a = int(n[:x])
    b = int(n[x:])
    print(a + b)
    n = str(a + b)