class pais:
    def __init__(self, n):
        self.n = n
        self.o = 0
        self.p = 0
        self.b = 0

    def __gt__(self, v):
        sm = self.o + self.p + self.b
        vm = v.o + v.p + v.b
        if sm == vm:
            return self.n < self.n
        return sm > vm

n, m = map(int, input().split())
d = dict(zip(range(1, n+1), (pais(x) for x in range(1, n+1))))

for _ in range(1, m+1):
    o, p, b = map(int, input().split())
    d[o].o += 1
    d[p].p += 1
    d[b].b += 1

for i in sorted(d.values(), reverse=True):
    print(i.n, end=" ")
print()
