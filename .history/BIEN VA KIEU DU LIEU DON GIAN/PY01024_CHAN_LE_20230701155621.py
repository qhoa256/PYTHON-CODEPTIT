if __name__ == "__main__":
    t = int(input())
    while t != 0:
        a = list(map(int, input().split()))
        for x in a:
            print(type(x))