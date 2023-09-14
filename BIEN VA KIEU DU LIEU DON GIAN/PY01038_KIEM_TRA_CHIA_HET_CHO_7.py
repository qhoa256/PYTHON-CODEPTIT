if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        loop = 0
        ok = 0
        while loop < 1000:
            res = int(n) + int(n[: : -1])
            if int(n) % 7 == 0:
                ok = 1
                print(n)
                break
            if res % 7 == 0:
                ok = 1
                print(res)
                break
            n = str(res)
            loop += 1
        if ok == 0:
            print(-1)