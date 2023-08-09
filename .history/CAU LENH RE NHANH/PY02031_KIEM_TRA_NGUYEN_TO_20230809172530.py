prime = [True] * (10 ** 6 + 1)

def sieve():
    prime[0]
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    