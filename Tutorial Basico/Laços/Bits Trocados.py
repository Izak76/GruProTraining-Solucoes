n = 1 #Contador do teste
while True:
    v = int(input()) #Valor em bits
    if not v: #Se v = 0 (Valor falso)...
        break #encerra o loop
        
    print("Teste", n)
    for x in (50, 10, 5, 1): #Repete o mesmo processo com todas os valores de cédulas
        nc = v//x #Número de cédulas de x de modo que x*nc <= v
        v -= nc*x #Remove de v todo o valor já contabilizado
        print(nc, end=" ") #Imprime o número de cédulas

    print("\n") #Pula uma linha para o próximo caso de teste
    n += 1 #Incrementa o caso de teste
