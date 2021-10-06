n, c = map(int, input().split())

#Número de pessoas dentro do elevador
np = 0
#A capacidade foi excedida? (Por padrão, não(N))
ex = "N" 

for x in range(n):
    s, e = map(int, input().split())
    
    #Retira o número de pessoas que saíram do elevador
    np -= s
    #Acrescenta o número de pessoas que entraram no elevador
    np += e
    
    #Verifica o número atual de pessoas
    #Se o número de pessoas for maior que C,
    #o status de excessão capacidade torna-se sim (S).
    #Se em nenhum momento np > c, a variável ex
    #não mudará.
    if np > c:
        ex = "S"

print(ex) #Imprime se houve excessão de pessoas no elevador
