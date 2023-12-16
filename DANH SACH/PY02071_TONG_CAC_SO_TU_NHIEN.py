def Try(i, pos, sum):
    global v, x
    for j in range(pos, 0, -1):
        x[i] = j
        if j == sum:
            tmp = x[1:i+1]
            v.append(tmp)
        elif j < sum:
            Try(i + 1, j, sum - j)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = []
        x = [0] * 1001
        Try(1, n, n)
        
        print(len(v))
        for i in range(len(v)):
            print("(", end="")
            for j in range(len(v[i])):
                print(v[i][j], end="")
                if j != len(v[i]) - 1:
                    print(" ", end="")
            print(") ", end="")
        print()
