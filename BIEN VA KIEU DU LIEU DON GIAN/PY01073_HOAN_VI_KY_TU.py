from itertools import permutations

if __name__ == '__main__':
  s = input()
  a = permutations(s)
  for i in a:
    for j in i:
      print(j, end = '')
    print()