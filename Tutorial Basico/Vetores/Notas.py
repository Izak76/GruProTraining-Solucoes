input()
n = tuple(map(int, input().split()))

maior, cmaior = 0, 0
for x in set(n):
    ct = n.count(x)
    if ct > cmaior:
        maior = x
        cmaior = ct

    elif ct == maior and x > maior:
        maior = x

print(maior)
        
