def check(p):
    for i in a:
        if i//p < i//(p + 1) + 1:
            return 0
    return 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    s, ans = min(a), 0
    for i in range(s, 0, -1):
        if check(i):
            for j in range(n):
                ans += a[j]//(i+1)+ 1
            break
    print(ans)