if __name__ == "__main__":
    n = int(input())
    n = abs(n)
    while n > 9:
        sum = 0
        while n != 0:
            sum += n % 10
            n //= 10
        