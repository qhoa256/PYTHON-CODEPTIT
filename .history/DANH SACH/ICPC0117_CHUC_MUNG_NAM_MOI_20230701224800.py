if __name__ == "__main__":
    x = []
    t = int(input())
    while t != 0:
        s = input()
        if x.count(s) == 0:
            x.append(s)
    print(len(x))
