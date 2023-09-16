def check(s):
  a = s.count('A')
  b = s.count('B')
  c = s.count('C')
  return len(s) >= 3 and a * b * c > 0 and a <= b and b <= c

def Try (i, s, n, a):
  if i > n:
    return
  if check(s):
    a.append(s)
  if i < n:
    Try(i + 1, s + 'A', n, a)
    Try(i + 1, s + 'B', n, a)
    Try(i + 1, s + 'C', n, a)
if __name__ == "__main__":
  n = int(input())
  a = []
  Try(0, '', n, a)
  a.sort(key = lambda s: len(s))
  for x in a:
    print(x)
