from math import *

prime = [True] * (1001)

def sieve():
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(1001) + 1):
        if prime[i]:
            for j in range(i * i, 1001, i):
                prime[j] = False

if __name__ == "__main__":
    sieve()
    n, m = map(int, input().split())
    Max = 0
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    cnt = [0] * 1001
    for i in range(n):
        for j in range(m):
            if prime[a[i][j]]:
                Max = max(Max, a[i][j])
                cnt[Max] += 1
    if Max == 0:
        print('NOT FOUND')
    else:
        print(cnt[Max])
        for i in range(n):
            for j in range(m):
                if a[i][j] == Max:
                    print()
    