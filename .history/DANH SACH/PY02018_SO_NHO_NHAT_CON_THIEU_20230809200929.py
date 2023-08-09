if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    Max = max(a)
    ok = 0
    for x in range(Max + 1):
        if x not in a:
            print(x)
            ok = 1
            break
    if ok == 0: