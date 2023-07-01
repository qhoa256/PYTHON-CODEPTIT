if __name__ == "__main__":
    t = int(input())
    while t != 0:
        s = input()
        cnt = 1
        s += '@'
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                print(cnt,)