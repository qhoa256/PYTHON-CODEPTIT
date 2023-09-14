if __name__ == "__main__":
    a, K, N = map(int, input().split())
    begin = K - (a % K)
    end = N - a
    if begin > end:
        print(-1)
    else:
        for i in range(begin, end + 1, K):
            print(i, end=' ')