def split_keys(D, func):
	l = {}
	for item in D:
		if func(D[item]):
			if l:
				yield l
				l = {}

		else:
			l[item] = D[item]

	if l:
		yield l

def rindex(itr, item):
	return len(itr) - itr[::-1].index(item) - 1

def max_pts(D):
	int_max = tuple()
	pts_max = 0
	for d in D:
		dv = tuple(d.values())
		pmx = max(dv)
		if (pmx >= pts_max) and (pmx != 0): 
			dk = tuple(d.keys())[:rindex(dv, pmx)+1]
			if (pmx > pts_max) or ((pmx == pts_max) and (len(dk) > len(int_max))):
				int_max = dk
				pts_max = pmx

	return int_max

teste = 1
for n in iter(lambda: int(input()), 0):
	part = {}
	saldo = 0
	for p in range(1, n+1):
		x, y = map(int, input().split())
		saldo += x-y
		part[p] = saldo

		if saldo < 0:
			saldo = 0

	sp = split_keys(part, lambda x: x < 0)
	mx = max_pts(sp)
	out = "nenhum" if not mx else f"{mx[0]} {mx[-1]}"
	print(f"Teste {teste}\n{out}\n")
	teste += 1
