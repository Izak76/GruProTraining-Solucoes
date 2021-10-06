from math import log10

b = 0 #"Tamanho" da maior quantidade de bactérias
k = 0 #Tipo de bactéria "dona" de b
for x in range(int(input())):
    d, c = map(int, input().split()) #Obtém os valores de entrada
    z = c*log10(d)
    if z > b: #Se este tipo é maior do que a atual...
        b = z #b agora é este tipo de bactéria
        k = x #k assume o novo tipo de bactéria 
        
print(k)

'''
Neste problema, a quantidade final de bactérias é dada por d**c.

Pensei em comparar estes resultados diretamente, atribuindo z = d**c, no entanto,
havia casos em que z assumia valores extremamante altos, devido a sua natureza
exponencial. Comparar valores muito altos dá muito trabalho, o que reflete no tempo
de execução, resultando no erro "Tempo limite excedido".

Para contornar isso, recorri ao logaritmo, mais especificamente a propriedade:
log(a**c, base=b) == c*log(a, base=b).

Portanto, em vez de z = d**c, utilizei z = c*log10(d) (logaritmo de base 10), o que
reduziu drasticamente o tamanho dos númeos analisados, facilitando muito o trabalho
de comparação, e consequentemente, reduzindo o tempo de execução.
'''
