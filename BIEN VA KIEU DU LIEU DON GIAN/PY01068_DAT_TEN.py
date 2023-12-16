from itertools import combinations

if __name__ == "__main__":
  n, k = map(int, input().split())
  s = set(input().split())
  a = list(s)
  a.sort()
  comb = combinations(a, k)
  for i in comb:
    for j in i:
      print(j, end = ' ')
    print()
