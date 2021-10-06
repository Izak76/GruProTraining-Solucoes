x, y = map(int, input().split())
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())

ps = []
A = (xa, ya)
B = (xb, yb)
for a in A:
    for b in B:
        ps.append(a+b <= x and max(A[A.index(a)-1], B[B.index(b)-1]) <= y)
        ps.append(a+b <= y and max(A[A.index(a)-1], B[B.index(b)-1]) <= x)

res = "S" if any(ps) else "N"
print(res)
