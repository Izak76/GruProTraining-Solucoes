def verificar(sud):
    for l in sud:
        if len(frozenset(l)) < 9:
            return "NAO"

    for c in range(9):
        if len({sud[l][c] for l in range(9)}) < 9:
            return "NAO"

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            m = [{sud[a][b] for b in range(y, y+3)} for a in range(x, x+3)]
            if len(m[0]|m[1]|m[2]) < 9:
                return "NAO"

    return "SIM"

for k in range(1, int(input())+1):
    sud = [input().split() for _ in range(9)]
    print(f"Instancia {k}\n{verificar(sud)}\n")
