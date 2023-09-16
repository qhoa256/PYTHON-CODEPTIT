alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n, base = map(int, input().split())
    ans = ''
    while n > 0:
        ans += alpha[n % base]
        n //= base
    print(ans[::-1])