def arredores(x, y):
    for z in range(x-1, x+2, 2):
        if mapa[z][y] == '.':
            return True

    for z in range(y-1, y+2, 2):
        if mapa[x][z] == '.':
            return True
        
    return False

mapa = []
m, n = map(int, input().split())

mapa.append('.'*(n+2))
for _ in range(m):
    mapa.append("".join(['.', input(), '.']))
mapa.append('.'*(n+2))

c = 0
for x in range(1, m+1):
    for y in range(1, n+1):
        if mapa[x][y] == "#" and arredores(x, y):
            c += 1

print(c)
