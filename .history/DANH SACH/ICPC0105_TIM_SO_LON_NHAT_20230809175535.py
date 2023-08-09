import re
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        a = list(map(int, re.findall(r'\d+', s)))
        if len(a) > 0:
            print(max(a))