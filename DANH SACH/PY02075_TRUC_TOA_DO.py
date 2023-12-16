class DoanThang:
    def __init__(self, bg, en):
        self.bg = bg
        self.en = en

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = []
        for _ in range(n):
            s = list(map(int, input().split()))
            a.append(DoanThang(s[0], s[1]))
        a.sort(key = lambda x: x.en)
        cnt = 1
        tmp = a[0].en
        for i in range(1, n):
            if tmp <= a[i].bg:
                cnt += 1
                tmp = a[i].en
        print(cnt)