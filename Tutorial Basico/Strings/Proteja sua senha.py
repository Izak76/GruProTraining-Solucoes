n = int(input())
t = 1

while n:
    pwds = []
    for _ in range(n):
        a = input().split()
        d = {}
        for x, y, z in zip(('A', 'B', 'C', 'D', 'E'), a[:-6:2], a[1:-6:2]):
            d[x] = (y, z)

        pwd = []
        for x in a[-6:]:
            pwd.append(d[x])
        pwds.append(pwd)
    
    print(f"Teste {t}")
    for x in zip(*pwds):
        k = frozenset(x[0])
        for y in x[1:]:
            k &= frozenset(y)

        k ,= k
        print(k, end=" ")

    print("\n")
    t += 1
    n = int(input())
