n, k = map(int, input().split())
balas = dict.fromkeys(range(1, k+1), 0)
for x in map(int, input().split()):
	balas[x] += 1

print(min(balas.values()))