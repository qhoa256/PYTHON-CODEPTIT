MOD = 10**9 + 7
def powMod(a, b):
    if b == 0:
        return 1
    res = powMod(a, b // 2)
    if b % 2 == 1:
        return ((res % MOD) * (res % MOD) * (a % MOD)) % MOD
    else:
        return ((res % MOD) * (res % MOD)) % MOD
    
def decToBin(n):
    return str(bin(n))[2::]

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        res = 0 
        s = decToBin(k)
        for i in range(len(s)):
            if(s[i] == '1'): 
                res += powMod(n, len(s) - i - 1)
                res %= MOD 
        print(res)