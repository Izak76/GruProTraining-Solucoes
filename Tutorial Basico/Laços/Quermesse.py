n = int(input())
c = 1
while n:
    print(f"Teste {c}")
    k = 1
    for x in map(int, input().split()):
        if x == k:
            print(x, "\n")
            break
        k += 1
    c+=1
    n = int(input())
