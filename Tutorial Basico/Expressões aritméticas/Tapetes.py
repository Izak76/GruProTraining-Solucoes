#O resultado é a área do maior tapete de modo que, somados com os N-1 tapetes restantes de dimensões 1x1, seja igual ao L inicial.
l, n = map(int, input().split()) #Obtém os valores
l -= n-1 #Remove a medida dos n-1 tapetes 1x1
print(l**2+n-1) #Área do tapete maior + a área dos tapetes 1x1 restantes
