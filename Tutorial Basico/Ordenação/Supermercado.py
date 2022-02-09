#A solução deste problema está em tirar as medianas de todas as posições x e y, respectivamente, de todos os supermercados
#As duas medianas resultantes serão as coordenadas do depósito

#OBSERVAÇÃO IMPORTANTE: No exemplo do problema, o "Teste 1" está errado, pois a resposta correta seria "-1 0", e não "-2 0" 
def mediana(valores): #Função para tirar a mediana de um conjunto de números
    q = len(valores)
    valores = sorted(valores)

    if q%2:
        return valores[q//2]
    else:
        return (valores[q//2]+valores[q//2-1])//2

teste = 1 #Caso teste
for s in iter(lambda: int(input()), 0): #s = número de supermercados (mais detalhes, estude o funcionamento da função "iter")
    x, y = [], [] #Lista para guardar as posições x e y dos supermercados, respectivamente
    for _ in range(s):
        #Adiciona as posições x (a) e y (b) a suas respectivas listas
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    print(f"Teste {teste}\n{mediana(x)} {mediana(y)}\n") #Imprime uma sstring formatada com o caso de teste e as medianas de cada coordenada
    teste += 1 #Incrementa o caso de teste