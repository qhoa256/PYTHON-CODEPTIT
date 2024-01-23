if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        x, y, a = map(int, input().split())
        tmp = a // (x + y)
        thieu = a - (x + y) * tmp
        if thieu <= 0:
            print(tmp * x * 5)
        else:
            print(tmp * x * 5 + min(thieu * 5, 5 * x))