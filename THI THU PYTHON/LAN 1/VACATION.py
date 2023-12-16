n, m = map(int, input().split())
a = []
for _ in range(n): 
    a.append(input())
b = []
for _ in range(m):
    b.append(["x"] * n)
for i in range (m):
    for j in range (n): 
        b[i][j] = a[j][i]
res, tmp = 0, 0
for i in range (m):
    ok = 1
    for j in range(n):
        if b[i][j] != 'o':
            ok = 0
            break
    if ok == 1:
        tmp += 1
    else:
        res = max(res, tmp)
        tmp = 0
res = max(res, tmp)
print(res)