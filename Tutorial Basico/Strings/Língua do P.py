cod = input().split()
dec = []

for p in cod:
    s = "".join((p[x] for x in range(1, len(p)+1, 2)))
    dec.append(s)

print(" ".join(dec))