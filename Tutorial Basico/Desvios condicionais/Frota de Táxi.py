ca, cg, ra, rg = map(float, input().split())

a = ca/ra
g = cg/rg

if a < g:
	print("A")
else:
	print("G")