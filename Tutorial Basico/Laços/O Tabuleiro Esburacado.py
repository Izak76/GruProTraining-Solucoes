class Cavalo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.movs = dict(enumerate([(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)], 1))

    def __iter__(self):
        return iter((self.x, self.y))
    
    def mover(self, m):
        m = self.movs[m]
        self.x += m[0]
        self.y += m[1]
    
input()
bur = [(1, 3), (2, 3), (2, 5), (5, 4)]

c = Cavalo(4, 3)
count = 0
for x in map(int, input().split()):
    c.mover(x)
    count += 1
    if tuple(c) in bur:
        break
    
print(count)
