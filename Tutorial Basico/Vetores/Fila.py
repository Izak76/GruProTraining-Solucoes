input()  #Ignora a 1ª entrada, pois não será necessária
fila = dict.fromkeys(input().split(), True)  #Cria um dicionário com todas as pessoas da fila, com valores inicialmente verdadeiros
input()  #Ignora a 3ª entrada, pois não será necessária
for x in input().split():  #Precorre a lista formada por todas as pessoas que sairam
	fila[x] = False  #Todas as pessoas que sairam da fila agora ganham valor falso

nfila = filter(lambda y: fila[y], fila)  #Filtra a fila, permanecendo apenas as pessoas que ainda possuem valor verdadeiro
print(" ".join(nfila))  #Imprime o resultado do filtro