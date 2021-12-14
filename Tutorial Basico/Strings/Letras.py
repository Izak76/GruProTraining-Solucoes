l = input()
txt = input().split()

c = 0
for p in txt:
	if l in p:
		c += 1

print(f"{100*c/len(txt):.1f}")