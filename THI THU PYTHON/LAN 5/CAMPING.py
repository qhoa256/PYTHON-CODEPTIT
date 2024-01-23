if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    se = set()
    se.add(x)
    for tmp in a:
        se.add(tmp)
    cnt = 0
    ok = 0
    h = list(se)
    h.sort()
    for qhoa in h:
        cnt += 1
        if qhoa == x:
            ok = 1
            print(cnt)
    if ok == 0:
        print(cnt + 1)
