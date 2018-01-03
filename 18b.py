import utils
from queue import Queue


class Program:
    def __init__(self, index, instructions):
        self.index = index
        self.registers = dict()
        self.registers['p'] = self.index
        self.instructions = instructions
        self.queue = Queue()
        self.sends = 0
        self.pos = 0

    def send(self, value):
        programs[(self.index + 1) % len(programs)].queue_value(value)
        self.sends += 1
        if self.index == 1:
            print(f'{self.index}: {self.sends}x sends')

    def queue_value(self, value):
        self.queue.put(value)

    def receive(self, register):
        self.registers[register] = self.queue.get()

    def next(self):
        if self.pos >= len(self.instructions):
            return
        i = self.instructions[self.pos]
        action = i[0]
        try:
            x = int(i[1])
        except ValueError:
            x = i[1]
        if type(x) is int:
            vx = x
        else:
            if x not in self.registers:
                self.registers[x] = 0
            vx = self.registers[x]
        if len(i) > 2:
            try:
                y = int(i[2])
            except ValueError:
                y = i[2]
            if type(y) is int:
                vy = y
            else:
                if y not in self.registers:
                    self.registers[y] = 0
                vy = self.registers[y]
        # print(f'{self.index}: {self.pos}, {i}, {vx}')
        if action == 'snd':
            self.send(vx)
        if action == 'set':
            self.registers[x] = vy
        if action == 'add':
            self.registers[x] += vy
        if action == 'mul':
            self.registers[x] *= vy
        if action == 'mod' and vy is not 0:
            self.registers[x] %= vy
        if action == 'rcv':  # and vx is not 0:
            if self.queue.qsize() == 0:
                return
            self.receive(x)
        if action == 'jgz':
            if vx > 0:
                self.pos += vy
                return
        self.pos += 1


with utils.get_input(18) as f:
    input = [i.strip().split(' ') for i in f.readlines()]
    # input = [i.strip().split(' ') for i in ['snd 1', 'snd 2', 'snd p', 'rcv a', 'rcv b', 'rcv c', 'rcv d']]
    programs = [Program(i, input) for i in range(2)]
    while True:
        for p in programs:
            p.next()
