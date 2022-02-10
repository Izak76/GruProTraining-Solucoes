from math import hypot

def busca(item, lista):
    e = 0
    d = len(lista)-1
    while e <= d:
        m = (e+d)//2
        if lista[m] == item:
            break

        elif item < lista[m]:
            d = m-1

        elif item > lista[m]:
            e = m+1

    if lista[m] < item:
        m += 1

    return m

c, t = map(int, input().split())

r = tuple((int(input()) for _ in range(c)))
lr = len(r)

p = 0
for _ in range(t):
    h = hypot(*map(int, input().split()))
    p += lr - busca(h, r)

print(p)
