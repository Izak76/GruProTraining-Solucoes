n = int(input())
tab = [int(input()) for _ in range(n)]
tab.insert(0, 0)
tab.append(0)

ant, atl, prx = iter(tab), iter(tab), iter(tab)
for i in (atl, prx, prx):
	next(i)

for k in zip(ant, atl, prx):
	print(sum(k))