if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        p, q = input().split()
        x = min(p, q)
        y = max(p, q)
        x1min = 