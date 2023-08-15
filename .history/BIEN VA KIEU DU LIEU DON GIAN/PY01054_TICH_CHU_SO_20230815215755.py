if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        mul = 1
        for x in n:
            if x != '0':
                mul *= int(x)
