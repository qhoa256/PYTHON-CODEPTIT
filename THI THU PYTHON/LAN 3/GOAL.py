if __name__ == '__main__':
    res = []
    while True:
        try:
            a = list(map(int, input().split()))
            res += a
        except:
            break
    print(res)

    