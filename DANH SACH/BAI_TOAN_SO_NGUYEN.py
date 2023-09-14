if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        rev = str(n)
        print(rev[: : -1])
        