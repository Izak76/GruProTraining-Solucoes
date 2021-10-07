from math import hypot

s = 0
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    s += hypot(x2-x1, y2-y1)**2

print(int(s))
