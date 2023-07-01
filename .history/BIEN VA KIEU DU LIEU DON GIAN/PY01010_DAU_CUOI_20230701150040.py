if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = input()
        if n[: 2] == n[-2 : ]:
            print('YES')
        else:
            print('NO')