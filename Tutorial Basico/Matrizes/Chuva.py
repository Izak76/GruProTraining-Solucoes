n = int(input())
i = [list(map(int, input().split())) for _ in range(n)]
f = [list(map(int, input().split())) for _ in range(n)]

for x in range(n):
    for y in range(n):
        print(f[x][y] + i[x][y], end=" ")
    print()
