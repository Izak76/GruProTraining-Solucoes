n = int(input())
mapa = [input()[::1-2*(x%2)] for x in range(n)]
ncom = []
com = 0
for linha in mapa:
    for item in linha:
        if item == "o":
            com += 1
            
        elif item == "A":
            ncom.append(com)
            com = 0

ncom.append(com)
print(max(ncom))
