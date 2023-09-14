v = []
def init():
    v.append(1)
    idx = 1
    num = 1
    while len(v) < n:
        x = len(str(num + 1))
        tmp = v[idx - 1] * (10 ** x) + (num + 1)
        v.append(tmp)
        idx += 1
        num += 1

if __name__ == "__main__":
    n, k = map(int, input().split())
    init()
    res = 0
    for i in range(len(v)):
        if v[i] % k == 0:
            res += 1
    print(res)