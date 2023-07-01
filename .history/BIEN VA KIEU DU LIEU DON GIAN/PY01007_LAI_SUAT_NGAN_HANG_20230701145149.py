if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n, x, m = map(int, input().split())
        res = 0
        while n < m:
            n += n * 0.01
            res += 1
        print(res)
        
