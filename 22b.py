import utils


class Virus:
    def __init__(self, grid):
        self.grid = grid
        self.pos = [int(len(grid[0]) / 2), int(len(grid) / 2)]
        self.dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  #NESW
        self.dir = 0
        self.infected = 0

    def turn(self, t):
        self.dir = (self.dir + t) % len(self.dirs)

    def move(self):
        self.pos[0] += self.dirs[self.dir][0]
        self.pos[1] += self.dirs[self.dir][1]
        if self.pos[0] < 0:
            for row in self.grid:
                row.insert(0, False)
                self.pos[0] = 0
        if self.pos[0] >= len(self.grid[0]):
            for row in self.grid:
                row.append(False)
        if self.pos[1] < 0:
            self.grid.insert(0, [False] * len(self.grid[0]))
            self.pos[1] = 0
        if self.pos[1] >= len(self.grid):
            self.grid.append([False] * len(self.grid[0]))
        # print(self.dirs[self.dir], self.pos)


    def update(self):
        if self.grid[self.pos[1]][self.pos[0]] == 0:
            self.turn(-1)
        if self.grid[self.pos[1]][self.pos[0]] == 1:
            self.infected += 1
        if self.grid[self.pos[1]][self.pos[0]] == 2:
            self.turn(1)
        if self.grid[self.pos[1]][self.pos[0]] == 3:
            self.turn(2)
        self.grid[self.pos[1]][self.pos[0]] = (self.grid[self.pos[1]][self.pos[0]] + 1) % 4
        self.move()


with utils.get_input(22) as f:
    input = [[(int(c == '#') * 2) for c in i.strip()] for i in f.readlines()]
    # input = ['.........', '.........', '.........', '.....#...', '...#.....', '.........', '.........', '.........', '.........']
    # input = [[(int(c == '#') * 2) for c in i] for i in input]
    v = Virus(input)
    for i in range(10000000):
        v.update()
print(v.infected)