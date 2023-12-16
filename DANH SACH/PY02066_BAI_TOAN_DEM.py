if __name__ == "__main__":
    n = int(input())
    a = []
    while len(a) < n:
        tmp = list(map(int, input().split()))
        for x in tmp:
            a.append(x)
    num = range(1, max(a))
    ok = True
    for x in num:
        if x not in a:
            ok = False
            print(x)
    if ok == True:
        print("Excellent!")
