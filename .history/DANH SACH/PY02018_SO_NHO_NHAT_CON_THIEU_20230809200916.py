if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    Max = max(a)
    for x in range(Max + 1):
        if x not in a:
            print(x)
            break
    p