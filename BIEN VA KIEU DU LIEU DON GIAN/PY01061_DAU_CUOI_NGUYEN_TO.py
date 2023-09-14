from math import *

def prime(n):
    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return True
    if n % 2== 0 or n % 3 == 0:
        return False
    m = -1
    while m * m <= n:
        m += 6
        if n % m == 0 or n % (m + 2) == 0:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        if prime(int(n[:3])) and prime(int(n[-3:])):
            print("YES")
        else:
            print("NO")