i = 1
while True:
    try:
        n = int(input())
    except EOFError:
        break

    ps = {}
    for x in range(n):
        a, q = input().split()
        q = int(q)
        
        ps[q] = ps.get(q, []) + [a]

    rep = sorted(ps[sorted(ps)[0]])[-1]
    print(f"Instancia {i}\n{rep}\n")
    i += 1
    
