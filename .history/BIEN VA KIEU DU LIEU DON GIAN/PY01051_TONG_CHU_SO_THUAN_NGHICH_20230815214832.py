if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        sum = 0
        for x in n:
            sum += int(x)
        tmp = str(sum)
        if tmp == tmp[::]:
            print('ÝE')