def pairwise(iterable):
    i1 = iter(iterable)
    i2 = iter(iterable)
    next(i2)

    return zip(i1, i2)

n, m = map(int, input().split())
casas = dict(zip(map(int, input().split()), range(n)))
encms = list(map(int, input().split()))
encms.insert(0, next(casas.keys().__iter__()))

c = 0
for prv, cur in pairwise(encms):
    c += abs(casas[cur]-casas[prv])

print(c)