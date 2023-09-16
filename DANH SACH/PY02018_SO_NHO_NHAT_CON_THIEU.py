if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ok = 0
    for x in range(1, max(a) + 1):
        if x not in a:
            print(x)
            ok = 1
            break
    if ok == 0:
        print(n + 1)