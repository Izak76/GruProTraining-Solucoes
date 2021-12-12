def posicoes(lista, item):
	start = 0
	for _ in range(lista.count(item)):
		f = lista.index(item, start)+1
		yield str(f)
		start = f

getin = lambda: map(int, input().split())

a, v = getin()
teste = 1
while a|v:
	aeros = [0]*a
	for _ in range(v):
		x, y = getin()
		aeros[x-1] += 1
		aeros[y-1] += 1

	ae = posicoes(aeros, max(aeros))
	print("Teste {}\n{}\n".format(teste, " ".join(ae)))

	teste += 1
	a, v = getin()