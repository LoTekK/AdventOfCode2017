from pathlib import Path
import utils
import re
import random


towers = dict()
with utils.get_input(7) as f:
    input = [''.join(line.split()).split('->') for line in f if '->' in line]
    for i in input:
        towers[re.sub(r'\(.*', '', i[0])] = i[1].split(',')
    count = 0
    check = True
    while check:
        tower_check = random.choice(list(towers.keys()))
        print(count, tower_check)
        count = 0
        for key, vals in towers.items():
            if tower_check in vals:
                tower_check = key
                break
            count += 1
            if count == len(towers.items()):
                check = False

print(tower_check)