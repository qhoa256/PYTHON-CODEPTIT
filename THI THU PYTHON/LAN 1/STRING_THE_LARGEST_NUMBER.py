if __name__ == "__main__":
    s = input()
    a = []
    for x in s:
        while a and x > a[-1]:
            a.pop()
        a.append(x)
    res = ""
    while len(a) > 0:
        res = a.pop() + res
    print(res)