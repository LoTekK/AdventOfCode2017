import math


class UlamSpiral:
    class Cell:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.value = 0

        def sum_neighbours(self, cells, limit):
            for y in range(self.y - 1, self.y + 2):
                if y < -limit or y >= limit:
                    continue
                for x in range(self.x - 1, self.x + 2):
                    if x < -limit or x >= limit:
                        continue
                    if x == self.x and y == self.y:
                        continue
                    self.value += cells[y + limit][x + limit].value
            print(f'[{self.x}, {self.y}]: {self.value}')

    def __init__(self, target):
        self.target = target
        self.limit = math.floor(math.ceil(math.sqrt(target)) / 2) + 1
        self.cells = list()
        for y in range(self.limit * 2 + 1):
            self.cells.append([UlamSpiral.Cell(x - self.limit, y - self.limit) for x in range(self.limit * 2 + 1)])
        self.radius = 0
        self.steps_per_side = 0
        self.step_counter = 0
        self.current = 1
        self.coord = [0, 0]
        self.dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        self.dir = 0
        self.get(0, 0).value = 1
        for i in range(target - 1):
            if not self.next():
                return

    def get(self, x, y):
        if x < -self.limit or x >= self.limit or y < -self.limit or y >= self.limit:
            return
        return self.cells[x + self.limit][y + self.limit]

    def get_current(self):
        return self.get(self.coord[0], self.coord[1])

    def next(self):
        self.current += 1
        self.step_counter += 1
        self.coord[0] += self.dirs[self.dir][0]
        self.coord[1] += self.dirs[self.dir][1]
        if self.current > pow(self.radius * 2 + 1, 2):
            self.radius += 1
            self.steps_per_side += 2
            self.step_counter = 1
            self.dir = (self.dir + 1) % len(self.dirs)
        if self.step_counter == self.steps_per_side and self.current < pow(self.radius * 2 + 1, 2):
            self.step_counter = 0
            self.dir = (self.dir + 1) % len(self.dirs)
        # self.cells[self.coord[1]][self.coord[0]].sum_neighbours(self.cells, self.limit)
        self.get(self.coord[0], self.coord[1]).sum_neighbours(self.cells, self.limit)
        if self.get(self.coord[0], self.coord[1]).value > self.target:
            return False
        return True

input = 289326
# input = 10
spiral = UlamSpiral(input)
print(spiral.get_current().value)
