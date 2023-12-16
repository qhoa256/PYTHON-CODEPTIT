def isReversible(n):
    res = str(n)
    return res == res[::-1] and len(res) >= 2

if __name__ == "__main__":
    n, m = map(int, input().split())
    Max = 0
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if isReversible(a[i][j]):
                Max = max(Max, a[i][j])
    if Max == 0:
        print('NOT FOUND')
    else:
        print(Max)
        for i in range(n):
            for j in range(m):
                if a[i][j] == Max:
                    print("Vi tri [", i,"][",j,"]", sep = '', end = '\n')
    