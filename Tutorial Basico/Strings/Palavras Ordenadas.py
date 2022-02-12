def ordenado(string):
    s1 = iter(string)
    s2 = iter(string)
    next(s2)
    for a, b in zip(s1, s2):
        if b <= a:
            return False

    return True

for _ in range(int(input())):
    palavra = input()
    r = "O" if ordenado(palavra.lower()) else "N"
    print(f"{palavra}: {r}")