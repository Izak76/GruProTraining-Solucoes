p1, c1, p2, c2 = map(int, input().split())

a1 = p1*c1
a2 = p2*c2
s = 0

if a1 < a2:
    s = 1
elif a1 > a2:
    s = -1

print(s)