#Ignora a 1ª entrada, pois não será necessária
input()
#Cria um dicionário com todas as pessoas da fila, com valores inicialmente verdadeiros
fila = dict.fromkeys(input().split(), True)
#Ignora a 3ª entrada, pois não será necessária
input()
#Precorre a lista formada por todas as pessoas que sairam
for x in input().split():
	#Todas as pessoas que sairam da fila agora ganham valor falso
	fila[x] = False

#Filtra a fila, permanecendo apenas as pessoas que ainda possuem valor verdadeiro
nfila = filter(lambda y: fila[y], fila)
#Imprime o resultado do filtro
print(" ".join(nfila))