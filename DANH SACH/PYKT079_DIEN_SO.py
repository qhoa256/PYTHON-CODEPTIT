if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    begin, end = min(a), max(a)
    se = set(a)
    print(max(a) - min(a) + 1 - len(se))