import utils
import re


factors = {'A': 16807, 'B': 48271}
divisor = 2147483647
num_steps = 40000000
matches = 0
with utils.get_input(15) as f:
    input = {re.sub(r'.*\s', '', k.strip()): int(v.strip()) for (k, v) in [l.split('starts with') for l in f.readlines()]}
    # input['A'] = 65
    # input['B'] = 8921
    for i in range(num_steps):
        comp = list()
        for k, v in input.items():
            input[k] = (input[k] * factors[k]) % divisor
            comp.append(format(input[k], '016b')[-16:])
        if comp[0] == comp[1]:
            matches += 1
            print(i, matches)
print(matches)