if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        a = list(map(int, input().split()))
        if len(a) == 1:
            p = a[0]
            q = int(input())
        else:
            p, q = a[0], a[1]
        x = min(p, q)
        y = max(p, q)
        s1 = input()
        s2 = input()
        small1, small2 = s1.replace(y, x), s2.replace(y, x)
        big1, big2 = s1.replace(x, y), s2.replace(x, y)
        print(int(small1) + int(small2), int(big1) + int(big2))