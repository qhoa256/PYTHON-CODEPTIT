from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Area(self):
        if max(a, b, c) * 2 >= a + b + c:
            return 'INVALID'
        res = sqrt((a+b+c) * (a+b-c) * (-a+b+c) * (a-b+c)) / 4
        return f"{res:.2f}"


arr, j = [], 0
t = int(input())
for _ in range(t):
    arr += [float(i) for i in input().split()]

for i in range(t):
    s = arr[:]
    p1, p2, p3 = (
        Point(s[j], s[j + 1]),
        Point(s[j + 2], s[j + 3]),
        Point(s[j + 4], s[j + 5]),
    )

    j += 6
    a = p1.distance(p2)
    b = p1.distance(p3)
    c = p2.distance(p3)
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        print("INVALID")
    else:
        triangle = Triangle(a, b, c)
        print(triangle.Area())

# 3
# 0 0 0 5 0 199
# 1 1 1 1 1 1
# 0 0 0 5 5 0