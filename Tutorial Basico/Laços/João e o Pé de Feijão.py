def is_kaprekar(x):
    u = str(x**2)
    for y in range(1, len(u)):
        u0 = int(u[:y])
        u1 = u[y:]
        
        if len(u1) == u1.count('0'):
            return False
        u1 = int(u1)

        if u0+u1 == x:
            return True
        
    return False

while True:
    n = int(input())
    if not n:
        break
    
    elif n==1 or is_kaprekar(n):
        print("%i: S"%n)

    else:
        print("%i: N"%n)
        

    
