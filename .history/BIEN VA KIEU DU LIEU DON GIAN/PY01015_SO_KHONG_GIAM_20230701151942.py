if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = input()
        ok = True
        for i in range(1, n):
            if n[i] < n[i - 1]:
                ok = False
                break
        if ok:
            print('YES')
        else:
            print('NO')
        t -= 1