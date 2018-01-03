import utils


def move(fr, to):
    fr[:] = [fr[n] + to[n] for n in range(len(fr))]

dirs = dict()
dirs['n'] = [0, 1, -1]
dirs['s'] = [0, -1, 1]
dirs['ne'] = [1, 0, -1]
dirs['sw'] = [-1, 0, 1]
dirs['se'] = [1, -1, 0]
dirs['nw'] = [-1, 1, 0]

with utils.get_input(11) as f:
    max_dist = 0
    input = [n for n in f.read().strip().split(',')]
    # input = [n for n in 'ne,ne,ne'.strip().split(',')]
    pos = [0, 0, 0]
    for step in input:
        move(pos, dirs[step])
        max_dist = max(max_dist, sum(abs(n) for n in pos if n < 0))
print(max_dist)
