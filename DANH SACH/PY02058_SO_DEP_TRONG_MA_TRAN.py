if __name__ == "__main__":
    n, m = map(int, input().split())
    Min, Max = 10000000, 0
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
        Max = max(Max, max(a[i]))
        Min = min(Min, min(a[i]))
    luckyNum = Max - Min
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == luckyNum:
                cnt += 1
    if cnt == 0:
        print('NOT FOUND')
    else:
        print(luckyNum)
        for i in range(n):
            for j in range(m):
                if a[i][j] == luckyNum:
                    print("Vi tri [", i,"][",j,"]", sep = '', end = '\n')