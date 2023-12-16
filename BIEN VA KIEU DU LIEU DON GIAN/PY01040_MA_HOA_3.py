p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def num(s):
    return ord(s) - 65

def rotate(s):
    sum = 0
    for x in s: sum += num(x)
    res = ""
    for x in s: res += p[(num(x) + sum) % 26]
    return res

def drm(s1, s2):
    n = len(s1)
    res = ""
    for i in range(n): 
        res += p[(num(s1[i]) + num(s2[i])) % 26]
    return res

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        n = len(s) // 2

        s1 = s[:n]
        s2 = s[n:]

        s1 = rotate(s1)
        s2 = rotate(s2)

        print(drm(s1, s2))