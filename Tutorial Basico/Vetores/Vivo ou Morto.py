p, r = map(int, input().split())
teste = 1
while p:
	x = list(map(int, input().split()))
	for _ in range(r):
		d = list(map(int, input().split()))
		n, j = d[:2]
		d_ = d[2:]
		for i in range(n):
			if j != d_[i]:
				x[i] = -1
		x = list(filter(lambda k: k>-1, x))

	print(f"Teste {teste}\n{x[0]}\n")
	teste += 1
	p, r = map(int, input().split())