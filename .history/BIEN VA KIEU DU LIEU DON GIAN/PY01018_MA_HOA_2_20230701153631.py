P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    str = input()
    if str == '0':
        break
    k, s = str.split()
    k = int(k)
    res = ''
    for i in s:
        j = P.find(i)
        res += P[(j + k) % 28]
    print(res[])