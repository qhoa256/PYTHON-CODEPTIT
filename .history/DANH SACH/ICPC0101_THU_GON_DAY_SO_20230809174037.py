if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    while i < len(a) - 1:
        if (a[i] + a[i + 1]) % 2 == 0:
             del a[i]
             del a[i]
             if i > 0:
                 i -= 1
        else:
            i += 1
    print(len(a))