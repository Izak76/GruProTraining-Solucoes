class Jogador:
    def __init__(self, nome, *pontos):
        self.nome = nome
        self.total = sum(pontos) - max(pontos) - min(pontos)

    def __lt__(self, valor):
        if self.total == valor.total:
            return self.nome < valor.nome

        return self.total > valor.total

    def __str__(self):
        return f"{self.total} {self.nome}"

teste = 1
for j in iter(lambda: int(input()), 0):
    jgs = sorted((Jogador(input(), *map(int, input().split())) for _ in range(j)))
    jgds = {}
    for t in jgs:
        jgds[t.total] = jgds.get(t.total, []) + [t]

    c = 1
    print(f"Teste {teste}")
    for key, values in jgds.items():
        for v in values:
            print(c, v)

        c += len(values)

    print()
    teste += 1 