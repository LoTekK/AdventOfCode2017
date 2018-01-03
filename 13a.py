import utils


def update(scanners, dest):
    c = 0
    for i in range(dest):
        if i in scanners.keys():
            r = scanners[i][1] - 1
            if abs((i - r) % (2 * r) - r) == 0:
                c += i * scanners[i][1]
    return c

with utils.get_input(13) as f:
    cost = 0
    input = {int(k): [0, int(v)] for (k, v) in [l.split(':') for l in f.readlines()]}
    # input = {0: [0, 3], 1: [0, 2], 4: [0, 4], 6: [0, 4]}
    last = list(reversed(sorted(input.keys())))[0] + 1
    cost = update(input, last)
print(cost)