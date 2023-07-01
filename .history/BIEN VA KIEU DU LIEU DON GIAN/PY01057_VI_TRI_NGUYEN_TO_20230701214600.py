def primeDigit(n):
    return n == 2 or n == 3 or n == 5 or n == 7

def res(n):
    for i in range(len(n)):
        if primeDigits(int(n[i])):
            
if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = input()
        for i in range(len(n)):
