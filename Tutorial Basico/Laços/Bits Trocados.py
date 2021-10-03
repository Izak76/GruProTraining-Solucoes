n = 1
while True:
    v = int(input())
    if not v:
        break
        
    print("Teste", n)
    for x in (50, 10, 5, 1):
        nc = v//x
        v -= nc*x
        print(nc, end=" ")

    print("\n")
    n += 1
