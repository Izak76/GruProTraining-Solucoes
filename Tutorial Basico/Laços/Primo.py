def e_primo(x):
    if x == 2:
        return True
    
    if x<=1 or not x%2:
        return False

    k = int(x**0.5)+1
    for y in range(3, k, 2):
        if not x%y:
            return False

    return True

print("sim" if e_primo(int(input())) else "nao")
