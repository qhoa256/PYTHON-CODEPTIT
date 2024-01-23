def check(n):
    return n == n[::-1]
if __name__ == '__main__':
    l, r = map(int, input().split())
    if r < l:
        l, r = r, l
    res = []
    for i in range(l, r + 1):
        if check(str(i)):
            res.append(i)
    print(sum(res))

