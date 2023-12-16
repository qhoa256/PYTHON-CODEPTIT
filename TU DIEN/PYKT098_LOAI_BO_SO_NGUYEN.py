# def check(s): #Check xem có là số int không
# 	k = 0
# 	for i in s :
# 		if not i.isdigit(): return True
# 		k = k * 10 + int(i)
# 	if k <= 2147483647 and k >= -2147483648 : return False
# 	return True
#
# file = open('DATA.in', 'r')
# a = []
# for line in file:
# 	for i in line.split():
# 		if check(i) : a.append(i)
# for i in sorted(a) :
# 	print(i, end = ' ')

def check(n):
    for x in n:
        if not x.isdigit():
            return True
    if int(n) >= 10 ** 9:
        return True
    else:
        return False
if __name__ == '__main__':
    f = open('DATA.in', 'r')
    res = []
    for line in f:
        x = list(map(str, line.split()))
        for i in x:
            if check(i):
                res.append(i)
    res.sort()
    for x in res:
        print(x, end = ' ')