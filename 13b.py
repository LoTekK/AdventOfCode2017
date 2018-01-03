import utils


def update(scanners, dest, d):
    for i in range(dest):
        if i in scanners.keys():
            r = scanners[i][1] - 1
            if abs(((i + d) - r) % (2 * r) - r) == 0:
                return False
    return True

with utils.get_input(13) as f:
    cost = 0
    input = {int(k): [0, int(v)] for (k, v) in [l.split(':') for l in f.readlines()]}
    # input = {0: [0, 3], 1: [0, 2], 4: [0, 4], 6: [0, 4]}
    last = list(reversed(sorted(input.keys())))[0]
    delay = 0
    while not update(input, last + 1, delay):
        delay += 1
        print(delay)
        pass

print(delay)