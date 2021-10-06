while True:
    n, p = map(int, input().split())
    if (not n) and (not p):
        break
    
    np = n//p + int(bool(n%p))
    j = "Poo{o}dle"
    k = (np-6)
    if k > 14:
        k = 14
    
    print(j.format(o="o"*k))
