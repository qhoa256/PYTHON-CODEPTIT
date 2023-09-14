def check(n):
    if n != n[: : -1]:
        return False
    tmp = int(n)
    while tmp > 0:
        if (tmp % 10) not in [0, 2, 4, 6, 8]:
            return False
        tmp //= 10
    return len(n) % 2 == 0
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        for i in range(22, n, 2):
            if check(str(i)):
                print(i, end = ' ')
        print()
