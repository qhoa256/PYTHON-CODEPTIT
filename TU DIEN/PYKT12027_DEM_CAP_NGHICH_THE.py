if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                res += 1
    print(res)
