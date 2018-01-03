class UlamSpiral:
    def __init__(self, target):
        self.radius = 0
        self.steps_per_side = 0
        self.step_counter = 0
        self.current = 1
        self.coord = [0, 0]
        self.dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        self.dir = 0
        for i in range(target - 1):
            self.next()

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
        print(self.current, self.coord)


input = 289326
spiral = UlamSpiral(input)
print(abs(sum(spiral.coord)))
