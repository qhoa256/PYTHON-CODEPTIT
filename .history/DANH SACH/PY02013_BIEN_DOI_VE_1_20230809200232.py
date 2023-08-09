if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        if n == 0:
            break
        cnt = 1
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
            cnt += 1
        