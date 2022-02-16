#Esta solução foi corrigida e aceita utilizando os casos de teste originais da OBI,
#pois a solução em Python 3 por motivos desconhecidos dá "Resposta errada" no SPOJ.

#Os casos de teste podem ser baixados em: https://olimpiada.ic.unicamp.br/static/extras/obi2014/gabaritos/2014f2p2_notas.zip
#Para uma solução que passe pelo SPOJ, aqui está a versão em C++: https://bit.ly/3GO7ezy

input()
cont = {}

for x in map(int, input().split()):
    cont.setdefault(x, 0)
    cont[x] += 1

print(max(cont, key=lambda x: (cont[x], x)))
