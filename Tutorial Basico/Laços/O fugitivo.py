from math import hypot

x, y = 0, 0
n, m = map(int, input().split())
ex = 0

for _ in range(n):
    c, d = input().split()
    d = int(d)

    if c == "N":
        y += d

    elif c == "S":
        y -= d

    elif c == "L":
        x += d

    elif c == "O":
        x -= d

    if hypot(x, y) > m:
        ex = 1
        break

print(ex)
