def move(n, a, b, c):
  if n == 1:
      print(f"{a} -> {c}")
  else:
      move(n - 1, a, c, b)
      move(1, a, b, c)
      move(n - 1, b, a, c)
if __name__ == "__main__":
  n = int(input())
  move(n,'A','B','C')