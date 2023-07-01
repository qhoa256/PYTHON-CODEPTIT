if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        sum = 0
        start = 1
        if n % 2 == 0:
            start = 2
        for i in range(start, n + 1, 2):
            sum += 1 / i
        print('{:.6f}'.format(sum))
    
