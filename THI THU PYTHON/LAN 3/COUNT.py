if __name__ == '__main__':
    n, q = map(int, input().split())
    a = [0] * 100001
    b = [0] * 100001
    c = [0] * 100001
    for i in range(1, n + 1):
        x = int(input())
        if x == 1:
            a[i] = a[i - 1] + 1
            b[i] = b[i - 1]
            c[i] = c[i - 1]
        if x == 2:
            a[i] = a[i - 1]
            b[i] = b[i - 1] + 1
            c[i] = c[i - 1]
        if (x == 3):
            a[i] = a[i - 1]
            b[i] = b[i - 1]
            c[i] = c[i - 1] + 1
    for i in range(q):
        x, y = map(int, input().split())
        print(a[y] - a[x - 1], b[y] - b[x - 1], c[y] - c[x - 1])
