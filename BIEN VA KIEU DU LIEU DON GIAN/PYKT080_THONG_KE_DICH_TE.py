dx = [-1,-1,-1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1,-1, 1,-1, 0, 1]

if __name__ == "__main__":
  n, m = map(int, input().split())
  a = []
  for i in range(n):
     a.append(list(map(int, input().split())))
  vs = [[False for i in range(m)] for j in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(m):
      if a[i][j] == -1:
          for k in range(8):
              inew, jnew = i + dx[k], j + dy[k]
              if inew >= 0 and inew < n and jnew >= 0 and jnew < m and vs[inew][jnew] == False:
                  cnt += a[inew][jnew]
                  vs[inew][jnew] = True
  print(cnt)