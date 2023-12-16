a = [1] * 10001
prime = []

def sieve():
    a[0] = a[1] = 0
    for i in range(2, 10001) :
        if a[i] == 1 :
            for j in range(i * i, 10001, i):
                a[j] = 0
            prime.append(i)

if __name__ == "__main__":
    sieve()
    n = int(input())
    list = list(map(int, input().split()))
    ans = 0
    for i in list:
        tmp = 10**9
        for j in prime:
            tmp = min(tmp, abs(i - j))
        ans = max(ans, tmp)
    print(ans)