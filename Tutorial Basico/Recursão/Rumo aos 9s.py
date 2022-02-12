somalg = lambda n: sum(map(int, str(n)))
for x in iter(lambda: int(input()), 0):
    xback = x
    
    if x%9:
        print(f"{x} is not a multiple of 9.")
        continue

    grau = 1
    for y in iter(lambda: somalg(x), 9):
        grau += 1
        x = y

    print(f"{xback} is a multiple of 9 and has 9-degree {grau}.")