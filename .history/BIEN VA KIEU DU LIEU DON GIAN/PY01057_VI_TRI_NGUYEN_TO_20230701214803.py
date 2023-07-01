def primeDigit(n):
    return n == 2 or n == 3 or n == 5 or n == 7

def res(n):
    for i in range(len(n)):
        if primeDigits(int(n[i])):
            if primeDigits(int(i)) == False:
                return False
        if primeDigits(int(n[i])) == False:
            if primeDigits(int(i)):
                return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = input()
        if res(n):
            print('YES')
        else:
            print('NO')