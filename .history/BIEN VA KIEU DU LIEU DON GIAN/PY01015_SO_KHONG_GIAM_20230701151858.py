if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = input()
        for i in range(1, n):
            if n[i] < n[i - 1]