n, k = map(int, input().split())
alunos = [input() for _ in range(n)]
alunos.sort()
print(alunos[k-1])