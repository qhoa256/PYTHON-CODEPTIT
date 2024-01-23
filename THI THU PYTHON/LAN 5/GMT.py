if __name__ == '__main__':
    h, m, a, b = map(int, input().split())
    h = h - a + b
    if h > 23:
        h -= 24
    elif h < 0:
        h += 24
    print(h, m)