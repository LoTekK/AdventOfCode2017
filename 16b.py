import utils
import time


def spin(l, n):
    a = int(n[0])
    l[:] = l[-a:] + l[:-a]


def exchange(l, m):
    a = int(m[0])
    b = int(m[1])
    l[a], l[b] = l[b], l[a]


def partner(l, m):
    a = l.index(m[0])
    b = l.index(m[1])
    l[a], l[b] = l[b], l[a]


def dance(l, move):
    move = [move[0], move[1:].split('/')]
    if move[0] == 's':
        spin(l, move[1])
    if move[0] == 'x':
        exchange(l, move[1])
    if move[0] == 'p':
        partner(l, move[1])


with utils.get_input(16) as f:
    programs = [c for c in 'abcdefghijklmnop']
    start_state = list(programs)
    # programs = [c for c in 'abcde']
    input = f.read().split(',')
    # input = ['s1', 'x3/4', 'pe/b']
    step_count = 0
    step = 0
    while step_count == 0:
        for i in input:
            dance(programs, i)
            if programs == start_state:
                print(f'{step + 1} steps before repeat')
                step_count = step + 1
                break
        step += 1
    for step in range(40):
        for i in input:
            dance(programs, i)
print(''.join(programs))
