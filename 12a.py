import utils


def get_zero_children(programs, key, zlist):
    for p in programs[key]:
        if p in zlist and key not in zlist:
            zlist.append(key)
        if p not in zlist:
            zlist.append(p)
            get_zero_children(programs, p, zlist)

inputs = dict()
with utils.get_input(12) as f:
    input = [''.join(i.strip().split()) for i in f.readlines()]
    for i in input:
        i = i.split('<->')
        i[0] = int(i[0])
        i[1] = [int(ii) for ii in i[1].split(',')]
        inputs[i[0]] = i[1]
    inputs = {0: [2], 1: [1], 2: [0, 3, 4], 3: [2, 4], 4: [2, 3, 6], 5: [6], 6: [4, 5]}
    zero_list = [0]
    get_zero_children(inputs, 0, zero_list)

count = 0
groups = []
for i in range(len(inputs)):
    zero_list = []
    get_zero_children(inputs, i, zero_list)
    if sorted(zero_list) not in groups:
        groups.append(sorted(zero_list))

for g in groups:
    print(g)
print(len(groups))