p, r = map(int, input().split())

x = "C"
if p:
    if r:
        x = "A"
    else:
        x = "B"

print(x)
