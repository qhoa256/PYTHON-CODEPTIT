def check(n):
    if len(n) % 2 == 0:
        return False
    if n[0] == n[1]:
        return False
    for i in range(2, len(n), 2):
        if n[i] != n[0]:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        if check(n):
            print('YES')
        else:
            print('NO')
