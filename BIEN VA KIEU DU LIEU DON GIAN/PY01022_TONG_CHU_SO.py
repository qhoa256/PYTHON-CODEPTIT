def trans(s):
    n = 0
    for x in s:
        n += ord(x) - ord('0')
    return str(n)
if __name__ == "__main__":
    s = input()
    if len(s) == 1:
        print(1)
    else:
        cnt = 0
        while len(s) > 1:
            s = trans(s)
            cnt += 1
        print(cnt)