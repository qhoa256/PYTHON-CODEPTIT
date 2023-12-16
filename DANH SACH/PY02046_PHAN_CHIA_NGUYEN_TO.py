from math import *

def prime(n):
    if n < 2: 
        return False
    for i in range (2, isqrt(n) + 1):
        if n % i == 0: 
            return False
    return True

if __name__ == '__main__':  
    n = int(input())
    tmp = list(map(int, input().split()))
    a = []
    for x in tmp:
        if x not in a:
            a.append(x)
    n = len(a)

    F = [0] * n
    F[0] = a[0]
    for i in range (1, n): 
        F[i] = F[i - 1] + a[i]
    ok = False
    for i in range (0, n - 1):
        if prime(F[i]) and prime(F[n - 1] - F[i]):
            ok = True
            print(i)
            break
    if ok == False: 
        print("NOT FOUND")