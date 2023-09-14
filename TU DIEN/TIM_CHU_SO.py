if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        n = int(input())
        t = 3 ** (1 / 2)
        res = (t + 2) ** n
        ans = int(res)
        ans %= 100
        if ans < 10:
            print(0, end = '')
        print(ans, end = "\n")
