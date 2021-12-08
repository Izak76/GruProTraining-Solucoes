cv, ce, cs, fv, fe, fs = map(int, input().split())

pc = 3*cv + ce
pf = 3*fv + fe

if pc > pf or (pc == pf and cs > fs):
    print("C")

elif pc < pf or (pc == pf and cs < fs):
    print("F")

else:
    print("=")
