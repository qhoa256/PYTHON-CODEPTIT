from math import *
from itertools import permutations

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = []
        for i in range (1, n + 1): 
            a.append(i)
        print(factorial(n))
        res = permutations(a)
        res1 = list(res)[::-1]
        for x in res1:
            for i in x: print(i, end = "")
            print(" ", end = "")
        print()
    