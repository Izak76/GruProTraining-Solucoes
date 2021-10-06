c = 1
while True:
    r = int(input())
    if not r:
        break

    a, b = 0, 0
    for _ in range(r):
        u = tuple(map(int, input().split()))
        a += u[0]
        b += u[1]

    venc = "Aldo" if a>b else "Beto"
    print(f"Teste {c}\n{venc}\n")
    c += 1
