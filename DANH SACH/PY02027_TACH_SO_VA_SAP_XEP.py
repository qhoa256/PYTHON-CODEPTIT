if __name__ == "__main__":
    t = int(input())
    res = []
    while t > 0:
        t -= 1
        s = input()
        for x in s:
            if x.isalpha():
                s = s.replace(x, " ")
        a = list(map(int, s.split()))
        for x in a:
            res.append(x)
    for x in sorted(res):
        print(x)
