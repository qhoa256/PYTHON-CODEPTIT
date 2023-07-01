def sumDigit(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum % 10 == 0
def two(n):
    s = str(n)
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) != 2:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t != 0:
