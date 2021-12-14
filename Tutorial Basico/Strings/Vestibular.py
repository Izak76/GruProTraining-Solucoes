n = int(input())
gab = input()
rsp = input()
for g, r in zip(gab, rsp):
	if r != g:
		n -= 1

print(n)