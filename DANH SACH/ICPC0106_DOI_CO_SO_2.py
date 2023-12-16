if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    b = int(input())
    s = input()
    x = int(s, 2)
    if b == 2: 
       print(s)
    elif b == 8: 
        res = str(oct(x))
        print(res[2::])
    elif b == 16: 
        res = str(hex(x))
        res = res[2::]
        print(res.upper())
    elif b == 4:
        st = []
        while(x):
            st.append(x % 4)
            x //= 4
        ans = st[::-1]
        for x in ans:
           print(x, end = '')
        print()