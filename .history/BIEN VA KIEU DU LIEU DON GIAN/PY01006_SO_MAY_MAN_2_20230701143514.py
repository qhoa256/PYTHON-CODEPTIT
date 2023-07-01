s = int(input())
for i in range(s):
    a = input()
    dem = 0
    for j in range(len(a)):
        if a[j]!='4' and a[j]!='7':
            dem = 1
            break
    if dem == 1:
        print("NO")
    else: 
        print("YES")