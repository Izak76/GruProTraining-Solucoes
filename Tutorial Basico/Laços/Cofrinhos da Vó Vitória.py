t = 1
while True:
    n = int(input())
    if not n:
        break
    
    d = 0
    print(f"Teste {t}")
    for _ in range(n):
        j, z = map(int, input().split())
        d = j-z+d
        print(d)
        
    print()
    t += 1
    
