if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        p, q = input().split()
        a = list(input().split())
        if len(a) == 1:
            x1 = a[0]
            x2 = input()
        else:
            x1, x2 = a[0], a[1]
        y = max(p, q)
        x = min(p, q)
        small1, small2 = x1.replace(y, x), x2.replace(y, x)
        big1, big2 = x1.replace(x, y), x2.replace(x, y)
        print(int(small1) + int(small2), int(big1) + int(big2))