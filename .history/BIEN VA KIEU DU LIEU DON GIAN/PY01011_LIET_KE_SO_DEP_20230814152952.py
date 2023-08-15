def check(n):
    qhoa = str(n)
    qhoa1 = qhoa[:]
    qhoa2 = qhoa[: : -1]
    cnt = 0
    while n != 0:
        tmp = n % 10
        cnt += 1
        if tmp != 0 and tmp != 2 and tmp != 4 and tmp != 6 and tmp != 8:
            return False
        n //= 10
    return cnt % 2 == 1 and qhoa[: : 1] == qhoa[: : -1]

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        for i in range(n):
            if check(i):
                print(i, end = ' ')
        t -= 1
