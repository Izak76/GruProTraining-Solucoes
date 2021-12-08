x0a, y0a, x1a, y1a = map(int, input().split())
x0b, y0b, x1b, y1b = map(int, input().split())

q0 = (x0b, y0b, x0a, y0a)
q1 = (x1a, y1a, x1b, y1b)
r = 1
for c0, c1 in zip(q0, q1):
    if c0 > c1:
        r = 0

print(r)
