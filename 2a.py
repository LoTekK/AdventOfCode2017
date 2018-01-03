import utils


input = list()
with utils.get_input(2) as f:
    for line in f:
        input.append(sorted([int(x) for x in line.split('\t')]))
    sum = 0
    for i in input:
        sum += abs(i[0] - i[len(i) - 1])
print(sum)
