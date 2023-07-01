def trans(s):
    n = 0
    for x in s:
        n += ord(x) - ord('0')
    return str(n)
if __name__ == "__main__":
    s = int(input())
    n = abs(n)
    if n >= 0 and n <= 9:
        print(1)
    else:
        cnt = 0
        while n > 9:
            cnt += 1
            sum = 0
            while n != 0:
                sum += n % 10
                n //= 10
            n = sum
        print(cnt)
