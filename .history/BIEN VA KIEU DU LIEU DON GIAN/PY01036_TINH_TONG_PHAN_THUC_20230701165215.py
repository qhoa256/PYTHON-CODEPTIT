if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        sum = 0
        if n % 2 == 0:
            for i in range(start, n + 1, 2):
                sum += 1 / i
        else:
            for i in range(1, n + 1, 2):
                sum += 1 / i
        print('{:.6f}'.format(sum))
    t -= 1
