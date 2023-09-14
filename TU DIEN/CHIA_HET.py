if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        a, b = map(int, input().split())
        if a % b == 0 or b % a == 0:
            print('YES')
        else:
            print('NO')