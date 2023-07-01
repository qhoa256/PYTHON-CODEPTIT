def trans(s):
    n = 0
    for x in s:
        n += ord(x) - ord('0')
    return str(n)
if __name__ == "__main__":
    s = int(input())
    cnt = 0
    while len(s) > 1
