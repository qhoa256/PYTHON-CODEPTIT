class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
    def transpose(self):
        trans = [[0 for y in range(n)] for x in range(m)]
        for i in range(n):
            for j in range(m):
                trans[j][i] = self.a[i][j]
        res = [[0 for y in range(n)] for x in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += self.a[i][k] * trans[k][j]
        for i in range(n):
            for j in range(n):
                print(res[i][j], end = ' ')
            print()


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n, m = map(int, input().split())
        mt = []
        for _ in range(n):
            tmp = list(map(int, input().split()))
            mt.append(tmp)
        a = Matrix(n, m, mt)
        a.transpose()
