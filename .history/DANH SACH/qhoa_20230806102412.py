if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    res = 1
    for x in a:
        res *= x
    v = []
    cnt = 0
    for i in range(1, m+1):
        tmp = 1
        b = list(map(int, input().split()))
        for x in b:
            tmp *= b
        if res % tmp == 0:
            cnt += 1
            v.append(tmp)





