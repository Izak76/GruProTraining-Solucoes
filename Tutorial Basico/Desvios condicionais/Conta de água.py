n = int(input())
total = 7 #Franquia de água

if 10 < n <= 30:
	total += n-10 #Quantidade em reais retirando os litros de franquia
	#Aqui o valor máximo é de R$20,00

elif 30 < n <= 100:
	total += 2*n-40 #Equivale à: total += 20+2*(n-30) (R$20,00 + 2 * (litros ainda não contados))
	#Aqui o valor máximo é de R$20,00 (contagem anterior) mais R$140,00 (contagem atual)

elif n > 100:
	total += 5*n-340 #Equivale à: total += 20+140+5*(n-100) (R$20,00 + R$140,00 + 5 * (litros ainda não contados))

print(total)