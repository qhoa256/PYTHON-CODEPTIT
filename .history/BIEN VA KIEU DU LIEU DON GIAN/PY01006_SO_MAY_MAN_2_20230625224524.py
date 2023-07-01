s = int(input())
for i in range(s):
    i=input()
    dem=0
    for j in range(len(i)):
        if i[j]!='4' and i[j]!='7':
            dem=1
            break
    if dem==1:
            print("NO")
    else: 
        print("YES")