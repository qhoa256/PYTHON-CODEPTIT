if __name__ == '__main__':
    m, n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ok = 0
    a.sort(reverse=True)
    for i in range(m - n + 1):
        tmp = a[i:i+n]
        Min, Max, Sum = tmp[n - 1], tmp[0], sum(tmp)
        if Max - Min <= k:
            ok = 1
            print(Sum)
            break
    if ok == 0:
        print('HUHU')