def check(n):
    for x in n:
        if x not in ['0', '1', '2', '3']:
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
