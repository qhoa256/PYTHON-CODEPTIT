if __name__ == "__main__":
  s1 = set(input().lower().split(' '))
  s2 = set(input().lower().split(' '))
  for x in sorted(s1.union(s2)):
    print(x, end = ' ')
  print()
  for x in sorted(s1.intersection(s2)):
    print(x, end = ' ')
  print()
