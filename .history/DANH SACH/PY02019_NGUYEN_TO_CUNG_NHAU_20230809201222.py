if __name__ == "__main__":
    n = int(input())
    a = sorted(list(map(int, input().split())))

    for i in range(n):
        for j in range(i + 1, n)