q = 0
for _ in range(int(input())):
    l, c = map(int, input().split())
    if l > c:
        q += c

print(q)
