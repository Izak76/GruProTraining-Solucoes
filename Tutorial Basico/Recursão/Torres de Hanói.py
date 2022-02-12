#OBS: O número mínimo de movimentos pode ser calculado por: 2**n-1
teste = 1 #Contador de casos teste
for n in iter(lambda: int(input()), 0): #Obtém os casos de teste (ver: funcionamento da função "iter")
	print(f"Teste {teste}\n{2**n-1}\n") #Imprime o resultado
	teste += 1 #Incrementa os casos de teste