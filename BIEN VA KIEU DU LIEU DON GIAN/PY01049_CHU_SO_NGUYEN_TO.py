from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        cnt, cntP = 0, 0
        for i in range(len(n)):
            if n[i] in ['2', '3', '5', '7']:
                cntP += 1
            else:
                cnt += 1
        if prime(len(n)) and cntP > cnt:
            print('YES')
        else:
            print('NO')