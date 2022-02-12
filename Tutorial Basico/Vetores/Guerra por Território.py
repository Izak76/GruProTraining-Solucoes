n = int(input())
secoes = tuple(map(int, input().split()))
total = sum(secoes)//2
soma = 0

for i in range(1, n+1):
    soma += secoes[i-1]
    if soma == total:
        print(i)
        break