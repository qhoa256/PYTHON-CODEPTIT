if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ans, res = 10**9, 0
    for x in a:
        cnt = 0 
        for y in a: 
            cnt += abs(x - y)
        if(cnt < ans):
            ans = cnt 
            p = x
    print(ans, p)