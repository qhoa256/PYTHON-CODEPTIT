if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        s += "@"
        res = ""
        ans = []
        for i in range(len(s)):
            if s[i].isdigit():
                res += s[i]
            else:
                if res != "":
                    ans.append(int(res))
                res = ""
        print(max(ans))