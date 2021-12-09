notas = list(map(float, input().split()))
notas.sort()
notas[0] = 0
notas[4] = 0
print(round(sum(notas), 1))