from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    if prime(len(n)) == False:
        return False
    cnt1, cnt2 = 0, 0
    for i in range(len(n)):
        if n[i] in ['2', '3', '5', '7']:
            cnt1 += 1
        else:
            cnt2 += 1
    return cnt1 > cnt2
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")
