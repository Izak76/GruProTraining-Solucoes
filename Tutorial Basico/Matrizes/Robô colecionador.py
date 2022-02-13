class Sentidos:
    def __init__(self, sent):
        self.sent = sent
        self.spin = ['N', 'L', 'S', 'O']

    def __add__(self, valor):
        self.sent = self.spin[(self.spin.index(self.sent)+valor)%4]

    def __sub__(self, valor):
        self.sent = self.spin[(self.spin.index(self.sent)-valor)%4]

    def __str__(self):
        return self.sent

class Mapa:
    def __init__(self, arr, n, m):
        self.mapa = arr
        self.figs = 0
        self.x_max = m
        self.y_max = n
        self.dirs = {
            'N': lambda: self.move_y(-1),
            'S': lambda: self.move_y(1),
            'L': lambda: self.move_x(1),
            'O': lambda: self.move_x(-1)
        }

        for y in range(n):
            for x in range(m):
                if arr[y][x] in ('N', 'S', 'L', 'O'):
                    self.x = x
                    self.y = y
                    self.ponto = Sentidos(arr[y][x])
                    return

    def move_x(self, d):
        x = self.x+d

        if (0 <= x) and (x < self.x_max):
            z = self.mapa[self.y][x]

            if z != "#":
                self.x = x

                if z == "*":
                    self.figs += 1
                    self.mapa[self.y][x] = "."

    def move_y(self, d):
        y = self.y+d

        if (0 <= y) and (y < self.y_max):
            z = self.mapa[y][self.x]

            if z != "#":
                self.y = y

                if z == "*":
                    self.figs += 1
                    self.mapa[y][self.x] = "."

    def cmd(self, c):
        if c == "D":
            self.ponto + 1

        elif c == "E":
            self.ponto - 1

        elif c == "F":
            self.dirs[str(self.ponto)]()

for n, m, s in iter(lambda: tuple(map(int, input().split())), (0, 0, 0)):
    mapa = Mapa([list(input()) for _ in range(n)], n, m)
    for c in input():
        mapa.cmd(c)

    print(mapa.figs)