if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        sum = 0
        for x in n:
            sum += int(x)
        print(sum)
        tmp = str(sum)
        res = tmp[::-1]
        if tmp == tmp[::]:
            print('YES')
        else:
            print('NO')