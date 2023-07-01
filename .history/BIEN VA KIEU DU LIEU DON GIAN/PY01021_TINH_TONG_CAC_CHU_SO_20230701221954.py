if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        a = []
        sum = 0
        for i in range(len(s)):
            if s[i].isdigit():
                a.append(s[i])
            else:

