if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        if n % 3 == 0:
            print('YES')
        else:
            print('NO')