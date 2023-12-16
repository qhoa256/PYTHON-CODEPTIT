if __name__ == "__main__":
    n = int(input())
    a = []
    while len(a) < n:
        x = list(map(int, input().split()))
        for tmp in x:
            a.append(tmp)
    pos = [0] * n
    even, odd = [], []
    for i in range(n):
        if a[i] % 2 == 1:
            odd.append(a[i])
        else:
            pos[i] = 1
            even.append(a[i])
    even.sort()
    odd.sort(reverse=True)
    i, j = 0, 0
    for k in range(n):
        if pos[k] == 1:
            print(even[i], end=' ')
            i += 1
        else:
            print(odd[j], end=' ')
            j += 1