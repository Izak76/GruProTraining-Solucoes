class Carro:
    def __init__(self, ncarro, voltas):
        self.carro = str(ncarro)
        self.total = sum(voltas)

    def __lt__(self, valor):
        return self.total < valor.total

    def __str__(self):
        return self.carro

n, m = map(int, input().split())
carros = [Carro(x, map(int, input().split())) for x in range(1, n+1)]
carros.sort()

for c in carros[:3]:
    print(c)