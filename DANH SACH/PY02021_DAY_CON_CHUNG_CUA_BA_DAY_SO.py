if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        x1, x2, x3, ok = 0, 0, 0, 0
        while x1 < n and x2 < m and x3 < k:
            if a[x1] == b[x2] and b[x2] == c[x3]:
                ok = 1 
                print(a[x1], end = ' ')
                x1 += 1
                x2 += 1
                x3 += 1
            elif a[x1] <= b[x2] and a[x1] <= c[x3]: x1 += 1 
            elif b[x2] <= a[x1] and b[x2] <= c[x3]: x2 += 1 
            else: x3 += 1 
        if ok == 0:
            print("NO", end = '')
        print()