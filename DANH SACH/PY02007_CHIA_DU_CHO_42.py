from math import *

if __name__ == '__main__':
    se = set({})
    while True:
        try:
            s = list(map(int, input().split()))
            for x in s:
                se.add(x % 42)
        except EOFError:
            break
    print(len(se))