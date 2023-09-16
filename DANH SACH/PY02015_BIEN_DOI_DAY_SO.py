if __name__ == "__main__":  
  while 1:
    x = list(map(int, input().split()))
    if sum(x) == 0:
       break
    res = 0
    while len(set(x)) != 1:
        res += 1
        tmp = x[0]
        for i in range(3):
            x[i] = abs(x[i] - x[i + 1])
        x[3] = abs(x[3] - tmp)
    print(res)