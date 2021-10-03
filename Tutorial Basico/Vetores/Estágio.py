#Este algoritmo não é baseado nos mostrados pelo enunciado!
#Toda lógica aqui foi construída "do zero"

n = int(input()) #Número de alunos da primeira turma
t = 1 #Número da turma

while n: #Enquanto n não assumir o valor 0 (falso)...
    mm = 0 #maior média
    a = [] #lista de alunos
    for _ in range(n):
        c, m = map(int, input().split()) #c = aluno; m = média
        if m > mm: #Se a média informada for maior que a média atual...
            mm = m #A média agora será a média informada
            a.clear() #O(s) aluno(s) com a média antiga é/são removido(s) da lsita

        #Se m for igual a mm, o aluno entrará na lista
        #Note que mesmo que a lista seja limpa, mm já está valendo m, logo, m == mm é verdadeiro
        if m == mm:
            a.append(c)

    print("Turma %i"%t) #Imprime a turma
    for p in a:
        print(p, end=' ') #Imprime todos os alunos
    print('\n')

    t += 1 #Incrementa o número da turma
    n = int(input()) #Novo valor de n para a próxima volta
