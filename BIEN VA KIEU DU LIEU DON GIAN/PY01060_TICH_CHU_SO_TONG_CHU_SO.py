if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        mul = 1
        sum = 0
        cnt = 0
        for i in range(len(n)):
            if i % 2 == 1:
                sum += int(n[i])
            else:
                if n[i] != '0':
                    cnt += 1
                    mul *= int(n[i])
        if cnt == 0:
            mul = 0
        print(mul, sum)
