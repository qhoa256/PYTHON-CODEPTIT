if __name__ == "__main__":
    x = []
    t = int(input())
    while t != 0:
        s = input()
        if x.count(s) == 0:
            x.append(s)
        t -= 1
    print(len(x))