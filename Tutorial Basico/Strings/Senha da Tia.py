n, m, a, k = map(int, input().split())
senha = input()

M = len(tuple(filter(lambda s: s.islower(), senha)))
A = len(tuple(filter(lambda s: s.isupper(), senha)))
K = len(tuple(filter(lambda s: s.isdigit(), senha)))

if all([len(senha) >= n, M >= m, A >= a, K >= k]):
	print("Ok =/")
else:
	print("Ufa :)")