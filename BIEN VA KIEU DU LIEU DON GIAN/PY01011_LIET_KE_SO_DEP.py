def tn(x):
    l, r = 0, len(x) - 1
    while l < r:
        if x[l] != x[r]:
            return False
        l += 1
        r -= 1
    return True
def check(n):
    x = str(n)
    digit = ['0', '2', '4', '6', '8']
    first = x[0]
    ok = 1
    for i in x:
        if i not in digit:
            ok = 0
            break
    return ok == 1 and len(x) % 2 == 0 and tn(x)

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        for i in range(n):
            if check(i):
                print(i, end = ' ')
        t -= 1
        print()
