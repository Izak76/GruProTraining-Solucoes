n, m = map(int, input().split())
pedras = ["0"]*n
for _ in range(m):
	p, d = map(int, input().split())
	p -= 1
	for i in range(p, -1, -d):
		pedras[i] = "1"

	for i in range(p, n, d):
		pedras[i] = "1"

print("\n".join(pedras))