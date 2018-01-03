from pathlib import Path
import utils
import re


def get_weight(d, sub_tower):
    return d[sub_tower][0] + sum(get_weight(d, t) for t in d[sub_tower][1])


def get_weights(d, sub_tower):
    if len(d[sub_tower][1]) is 0:
        return d[sub_tower][0]
    s = sum([get_weights(d, t) for t in d[sub_tower][1]])
    print(sub_tower, [get_weights(d, t) for t in d[sub_tower][1]], s / len(d[sub_tower][1]))
    return d[sub_tower][0] + s

bottom_tower = 'rqwgj'
towers = dict()
sums = dict()
with utils.get_input(7) as f:
    input = [''.join(line.split()).split('->') for line in f]
    for i in input:
        weight = int(re.search(r'(\d{1,9})', i[0]).group(0))
        towers[re.sub(r'\(.*', '', i[0])] = [weight, i[1].split(',') if len(i) > 1 else []]
    # for tower in towers[bottom_tower][1]:
    #     sums[tower] = get_weight(towers, tower)
    sums['nhrla'] = get_weights(towers, 'nhrla')

print(sums)
for i, w in enumerate(sums.values()):
    if list(sums.values()).count(w) == 1:
        print(list(sums.values())[len(sums) - i - 1] - w)