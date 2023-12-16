if __name__ == "__main__":
    s = input()
    t = input()
    k = int(input())
    if t.count(s) == k and k * len(s) == len(t):
        print('YES')
    else:
        print('NO')