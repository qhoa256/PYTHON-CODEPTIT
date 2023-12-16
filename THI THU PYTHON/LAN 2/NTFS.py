if __name__ == '__main__':
    t = int(input())
    d = t // 4096
    if t % 4096 > 0:
        d += 1
    print(d * 4)