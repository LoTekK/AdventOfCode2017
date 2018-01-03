import utils
import re


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'[{self.x}, {self.y}, {self.z}]'

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Particle:
    def __init__(self, i):
        i = [s.strip() for s in i.split(', ')]
        self.pos = Vector(*eval(re.sub(r'>', ']', re.sub(r'.*<', '[', i[0]))))
        self.velocity = Vector(*eval(re.sub(r'>', ']', re.sub(r'.*<', '[', i[1]))))
        self.acceleration = Vector(*eval(re.sub(r'>', ']', re.sub(r'.*<', '[', i[2]))))

    def __eq__(self, other):
        return self.pos.x == other.pos.x and self.pos.y == other.pos.y and self.pos.z == other.pos.z

    def update(self):
        self.velocity += self.acceleration
        self.pos += self.velocity

    def manhattan_distance(self):
        return self.pos.manhattan_distance()

def get_key(item):
    return item.manhattan_distance()


with utils.get_input(20) as f:
    particles = []
    input = f.readlines()
    for i in input:
        particles.append(Particle(i))
    for i in range(500):
        for p in particles:
            p.update()
        for p in particles:
            if particles.count(p) > 1:
                # print('collision')
                while particles.count(p) > 0:
                    particles.remove(p)
        print(len(particles))
    # for p in sorted(particles, key=get_key):
    #     print(p.manhattan_distance())
    # print(particles.index(sorted(particles, key=get_key)[0]))
