def horizontal():
    for l in matriz:
        yield sum(l)

def vertical():
    for y in range(m):
        s = 0
        for x in range(n):
            s += matriz[x][y]
        yield s
    
n, m = map(int, input().split())

matriz = [list(map(int, input().split())) for _ in range(n)]

print(max(max(vertical()), max(horizontal())))
