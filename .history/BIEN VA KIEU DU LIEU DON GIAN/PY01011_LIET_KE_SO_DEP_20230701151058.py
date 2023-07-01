def even(n):
    tmp = str(n)
    cnt = 0
    while n != 0:
        tmp = n % 10
        cnt += 1
        if tmp % 2 != 0:
            return False
        n //= 10
    return cnt % 2 == 1 and tmp[: : 1] == n[: : -1]

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        for i in range(n):
            if even(i):
                print(i, end = ' ')
        t -= 1
