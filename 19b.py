import utils
import re


class Grid:
    def __init__(self, i):
        self.cells = i
        self.h = len(self.cells)
        self.w = len(self.cells[0])
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # RDLU
        self.dir = 1  # D
        self.letters = []
        self.steps = 0

    def get(self, x, y):
        if y < 0 or y >= len(self.cells):
            return
        if x < 0 or x >= len(self.cells[y]):
            return
        cell = self.cells[y][x]
        if cell.isspace():
            return
        return cell

    def find_start(self):
        for x in range(self.w):
            cell = self.get(x, 0)
            if cell is None:
                continue
            return x

    def move(self, x, y):
        # print(x, y)
        self.steps += 1
        c = self.get(x, y)
        if c.isalpha():
            self.letters.append(c)
        nx = x + self.dirs[self.dir][0]
        ny = y + self.dirs[self.dir][1]
        next_cell = self.get(nx, ny)
        if next_cell:
            return [nx, ny]
        neighbours = [(i, d) for (i, d) in enumerate(self.neighbours(x, y)) if i % (len(self.dirs) / 2) != self.dir % (len(self.dirs) / 2)]
        for i, d in neighbours:
            if d is None:
                continue
            self.dir = i
            return [x + self.dirs[self.dir][0], y + self.dirs[self.dir][1]]
        return False

    def neighbours(self, x, y):
        return [self.get(x + d[0], y + d[1]) for d in self.dirs]


with utils.get_input(19) as f:
    input = Grid([re.sub(r'\n', '', i) for i in f.readlines()])
    n = input.move(input.find_start(), 0)
    while n:
        n = input.move(n[0], n[1])
    print(''.join(input.letters))
    print(input.steps)